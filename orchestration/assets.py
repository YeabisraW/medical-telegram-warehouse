from dagster import asset
from scripts.load_to_postgres import load_data_to_postgres
from scripts.config import logger

@asset
def raw_telegram_data():
    """Extract: Scrapes raw data from Telegram channels."""
    logger.info("Scraping Telegram...")
    return [1, 2, 3] # Mock data for graph

@asset(deps=[raw_telegram_data])
def postgres_raw_vault():
    """Load: Moves raw data into the PostgreSQL staging area."""
    logger.info("Loading to Postgres...")

@asset(deps=[postgres_raw_vault])
def dbt_mart_models():
    """Transform: Triggers dbt Medallion transformations (Bronze -> Silver -> Gold)."""
    logger.info("Executing dbt transformations...")

@asset(deps=[dbt_mart_models])
def yolo_enriched_data():
    """Enrich: Performs YOLOv8 object detection on images."""
    logger.info("Running AI detection...")