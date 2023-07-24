"""
script to load constance from enviorement,
with default values in case the variable name wasn't found
"""
import os

from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
BASE_URL = os.getenv("BASE_URL", "https://www.vox.com/news/")
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
DATABASE_NAME = os.getenv("DATABASE_NAME", "development")
