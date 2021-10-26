import os
import supervisely_lib as sly
from supervisely_lib.io.fs import mkdir


my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['modal.state.slyProjectId'])
INPUT_FILE = os.environ["modal.state.slyFile"]

storage_dir = my_app.data_dir
local_csv_path = os.path.join(storage_dir, "catalog.csv")
api.file.download(TEAM_ID, INPUT_FILE, local_csv_path)

IMAGE_URL_COL_NAME = 'Image URL'
PRODUCT_ID_COL_NAME = 'PRODUCT ID'
DEFAULT_DELIMITER = ','

img_dir = os.path.join(storage_dir, "img_dir")
mask_dir = os.path.join(storage_dir, "mask_dir")
mkdir(img_dir)
mkdir(mask_dir)

product_obj_class = sly.ObjClass("product", sly.Bitmap)
