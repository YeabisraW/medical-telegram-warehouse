import os
from dotenv import load_dotenv
import logging

# Load the .env file
load_dotenv()

class Config:
    # DB Settings
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASSWORD")
    
    # Paths
    RAW_DATA = os.getenv("RAW_DATA_PATH")
    YOLO_MODEL = os.getenv("YOLO_MODEL_PATH")

    @staticmethod
    def get_db_connection_string():
        return f"postgresql://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"

# Set up structured logging for the whole project
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MedicalPipeline")