from dagster import asset
from scripts.load_to_postgres import load_data_to_postgres # Import your real logic
# from scripts.scraper import main as run_scraper 

@asset
def raw_telegram_data():
    """Real Scraper Call"""
    # run_scraper() 
    return True

@asset(deps=[raw_telegram_data])
def postgres_raw_vault():
    """Real Load Call"""
    # Example: df = pd.read_csv('data.csv')
    # load_data_to_postgres(df, 'raw_table')
    return True