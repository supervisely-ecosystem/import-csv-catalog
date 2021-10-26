import csv
import globals as g
import functions as f
import supervisely_lib as sly


@g.my_app.callback("import-csv-catalog")
@sly.timeit
def import_csv_catalog(api: sly.Api, task_id, context, state, app_logger):
    project = api.project.create(g.WORKSPACE_ID, "CATALOG_CSV", sly.ProjectType.IMAGES, change_name_if_conflict=True)
    project_meta = sly.ProjectMeta(sly.ObjClassCollection([g.product_obj_class]))
    dataset = api.dataset.create(project.id, "ds0", change_name_if_conflict=True)
    with open(g.local_csv_path, "r") as catalog_csv:
        reader = csv.DictReader(catalog_csv, delimiter=g.DEFAULT_DELIMITER)
        reader = [row for row in reader]
        image_url_col_name, product_id_col_name = f.validate_csv_table(reader[0])
        progress = sly.Progress("Processing data from csv", len(reader))
        for batch in sly.batched(reader):
            image_paths = []
            image_names = []
            anns = []
            for row in batch:
                if len(row[image_url_col_name]) == 0:
                    continue
                image_name, image_path = f.process_image_by_url(api, row[image_url_col_name], app_logger)
                ann, project_meta = f.process_ann(row, project_meta, image_path, image_url_col_name, product_id_col_name)

                image_paths.append(image_path)
                image_names.append(image_name)
                anns.append(ann)

            api.project.update_meta(project.id, project_meta.to_json())
            images_infos = api.image.upload_paths(dataset.id, image_names, image_paths)
            images_ids = [image_info.id for image_info in images_infos]
            api.annotation.upload_anns(images_ids, anns)
            progress.iters_done_report(len(batch))

    g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": g.TEAM_ID,
        "WORKSPACE_ID": g.WORKSPACE_ID,
        "INPUT_FILE": g.INPUT_FILE
    })

    # Run application service
    g.my_app.run(initial_events=[{"command": "import-csv-catalog"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)
