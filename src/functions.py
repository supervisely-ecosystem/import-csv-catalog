import os
import requests
import numpy as np
import globals as g
import download_progress
import supervisely_lib as sly
from PIL import Image
from supervisely_lib.io.fs import download


def validate_csv_table(first_csv_row):
    col_names = [key for key in first_csv_row.keys()]
    if any(image_url_name in g.possible_image_url_col_names for image_url_name in col_names) \
            and any(product_id_name in g.possible_product_id_col_names for product_id_name in col_names):
        raise Exception("Required element is missing in the csv file")
    image_url_col_name = None
    product_id_col_name = None
    for name in col_names:
        if name.lower().startswith("image") and name.lower().endswith("url"):
            image_url_col_name = name
        if name.lower().startswith("product") and name.lower().endswith("id"):
            product_id_col_name = name

    return image_url_col_name, product_id_col_name


def download_file_from_link(api, link, save_path, file_name, progress_message, app_logger):
    response = requests.head(link, allow_redirects=True)
    sizeb = int(response.headers.get('content-length', 0))
    progress_cb = download_progress.get_progress_cb(api, g.TASK_ID, progress_message, sizeb, is_size=True)
    download(link, save_path, progress=progress_cb)
    download_progress.reset_progress(api, g.TASK_ID)
    app_logger.info(f'{file_name} has been successfully downloaded')


def get_image_size(path_to_img):
    im = Image.open(path_to_img)
    w, h = im.size
    return h, w


def process_image_by_url(api, image_url, app_logger):
    image_url = image_url.strip()
    image_name = os.path.basename(os.path.normpath(image_url)) + ".png"
    image_path = os.path.join(g.img_dir, image_name)
    download_file_from_link(api, image_url, image_path, image_name, f"Downloading {image_name}", app_logger)
    return image_name, image_path


def process_ann(csv_row, project_meta, image_path, image_url_col_name, product_id_col_name):
    product_id = csv_row[product_id_col_name].strip()
    image_shape = get_image_size(image_path)
    product_id_tag_meta = sly.TagMeta(product_id, sly.TagValueType.NONE)
    project_meta = project_meta.add_tag_meta(product_id_tag_meta)
    product_id_tag_col = sly.TagCollection([sly.Tag(product_id_tag_meta)])

    if sly.image.read(image_path, False).shape[2] == 3:
        mask = np.ones(image_shape, dtype=np.bool)
    else:
        im = Image.open(image_path)
        mask_path = os.path.join(g.mask_dir, "mask.png")
        im.convert('RGBA').split()[-1].save(mask_path, optimize=True)
        im = Image.open(mask_path)
        mask = np.asarray(im, dtype=np.bool)

    tag_info = csv_row
    del tag_info[image_url_col_name]
    del tag_info[product_id_col_name]

    label = sly.Label(sly.Bitmap(mask), g.product_obj_class, product_id_tag_col, description=tag_info)
    ann = sly.Annotation((image_shape[0], image_shape[1]), [label])
    return ann, project_meta
