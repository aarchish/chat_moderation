# backend service -> backend/utils.py
# envionment variables for backend service

import os

from dotenv import load_dotenv

# Load environment variables only once
load_dotenv()

# External service URLs
MODERATION_API_URL = os.getenv("MODERATION_API_URL", "http://localhost:8001/comment/")
DB_NAME = os.getenv("DB_NAME", "chat_moderation")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
