from dagster import asset
from dagster_dbt import dbt_assets, DbtCliResource, DbtProject
from pathlib import Path

# Path to your dbt project
DBT_PROJECT_DIR = Path(__file__).joinpath("..", "..", "medical_warehouse").resolve()
dbt_project = DbtProject(project_dir=DBT_PROJECT_DIR)
dbt_project.prepare_if_dev()

@dbt_assets(manifest=dbt_project.manifest_path)
def medical_dbt_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

@asset(deps=[medical_dbt_assets])
def final_pipeline_status():
    """This asset only runs after dbt is finished."""
    return "Success"