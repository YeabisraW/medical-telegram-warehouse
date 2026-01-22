import pandas as pd
from sqlalchemy import create_engine
from config import Config, logger  # Import your new centralized config

def load_data_to_postgres(df, table_name):
    """
    Loads a dataframe to postgres with error handling and logging.
    """
    if df.empty:
        logger.warning(f"Dataframe for {table_name} is empty. Skipping load.")
        return

    try:
        # Use the connection string from our Config class
        engine = create_engine(Config.get_db_connection_string())
        
        logger.info(f"Attempting to write {len(df)} rows to table '{table_name}'...")
        
        df.to_sql(table_name, engine, if_exists='append', index=False)
        
        logger.info(f"Successfully loaded data into {table_name}.")
        
    except Exception as e:
        # Structured error handling (Comment #4 requirement)
        logger.error(f"Critical error during database write to {table_name}: {e}")
        # In a real pipeline, you might want to re-raise or send an alert here