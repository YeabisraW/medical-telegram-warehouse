from dagster import Definitions, ScheduleDefinition, define_asset_job
from .assets import raw_telegram_data, postgres_raw_vault, dbt_mart_models, yolo_enriched_data

# Define a job that runs all assets in order
medical_pipeline_job = define_asset_job("medical_pipeline_job")

# Define the daily schedule (Requirement for Comment #2)
daily_refresh_schedule = ScheduleDefinition(
    job=medical_pipeline_job,
    cron_schedule="0 6 * * *", # Runs every day at 6:00 AM
)

defs = Definitions(
    assets=[raw_telegram_data, postgres_raw_vault, dbt_mart_models, yolo_enriched_data],
    schedules=[daily_refresh_schedule],
)