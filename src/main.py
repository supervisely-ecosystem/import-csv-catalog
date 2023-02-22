import csv
import globals as g
import functions as f
import supervisely_lib as sly


project = g.api.project.create(
    g.WORKSPACE_ID, g.project_name, sly.ProjectType.IMAGES, change_name_if_conflict=True
)
project_meta = sly.ProjectMeta(sly.ObjClassCollection([g.product_obj_class]))
dataset = g.api.dataset.create(project.id, "ds0", change_name_if_conflict=True)
unique_image_names = []
image_name_prefix = "1_"
with open(g.local_csv_path, "r") as catalog_csv:
    reader = csv.DictReader(catalog_csv, delimiter=g.DEFAULT_DELIMITER)
    reader = [row for row in reader]
    image_url_col_name, product_id_col_name = f.validate_csv_table(reader[0])
    progress = sly.Progress("processing CSV", len(reader))
    for batch in sly.batched(reader):
        image_paths = []
        image_names = []
        anns = []
        for row in batch:
            # if len(row[image_url_col_name]) == 0:
            #     continue

            try:
                image_name, image_path = f.get_image(row[image_url_col_name])
            except Exception as ex:
                sly.logger.warn(f"{ex}")
                continue

            ann, project_meta = f.process_ann(
                row, project_meta, image_path, image_url_col_name, product_id_col_name
            )

            image_paths.append(image_path)
            if image_name not in unique_image_names:
                unique_image_names.append(image_name)
                image_names.append(image_name)
            else:
                new_image_name = image_name_prefix + image_name
                unique_image_names.append(new_image_name)
                image_names.append(new_image_name)
            anns.append(ann)

        g.api.project.update_meta(project.id, project_meta.to_json())
        images_infos = g.api.image.upload_paths(dataset.id, image_names, image_paths)
        images_ids = [image_info.id for image_info in images_infos]
        g.api.annotation.upload_anns(images_ids, anns)
        progress.iters_done_report(len(batch))
