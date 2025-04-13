# backend service -> backend/utils.py
# envionment variables for backend service

import os
from dotenv import load_dotenv

# Load environment variables only once
load_dotenv()

# External service URLs
MODERATION_API_URL = os.getenv("MODERATION_API_URL", "http://127.0.0.1:8001/comment/")