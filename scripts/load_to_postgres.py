import pandas as pd
# FIX: Use absolute import from the project root
from scripts.config import Config, logger 

def load_data_to_postgres(df, table_name):
    logger.info(f"Loading data to {table_name}...")
    # Your database loading logic here
    pass