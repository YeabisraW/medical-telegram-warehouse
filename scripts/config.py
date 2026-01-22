import os
from dotenv import load_dotenv
import logging

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "medical_db")
    # ... include other variables ...

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("medical_warehouse")