import os
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
# PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
INPUT_FILE = os.environ["modal.state.slyFile"]

storage_dir = my_app.data_dir
local_csv_path = os.path.join(storage_dir, "catalog.csv")
api.file.download(TEAM_ID, INPUT_FILE, local_csv_path)

DEFAULT_DELIMITER = ','

possible_image_url_col_names = ["image url", "image-url", "image_url", "imageurl"]
possible_product_id_col_names = ["product id", "product-id", "product_id", "productid"]

img_dir = os.path.join(storage_dir, "img_dir")
mask_dir = os.path.join(storage_dir, "mask_dir")
mkdir(img_dir)
mkdir(mask_dir)

product_obj_class = sly.ObjClass("product", sly.Bitmap)
