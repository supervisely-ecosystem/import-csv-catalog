import os

import supervisely_lib as sly
from dotenv import load_dotenv
from supervisely.io.fs import get_file_name, mkdir

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


api = sly.Api.from_env()

TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()

INPUT_FILE = os.environ["modal.state.slyFile"]

project_name = get_file_name(INPUT_FILE)

storage_dir = sly.app.get_data_dir()
local_csv_path = os.path.join(storage_dir, "catalog.csv")
api.file.download(TEAM_ID, INPUT_FILE, local_csv_path)

DEFAULT_DELIMITER = ","

possible_image_url_col_names = ["image url", "image-url", "image_url", "imageurl"]
possible_product_id_col_names = ["product id", "product-id", "product_id", "productid"]

img_dir = os.path.join(storage_dir, "img_dir")
mask_dir = os.path.join(storage_dir, "mask_dir")
mkdir(img_dir)
mkdir(mask_dir)

# product_obj_class = sly.ObjClass("product", sly.Bitmap)
product_obj_class = sly.ObjClass("product", sly.Rectangle)
