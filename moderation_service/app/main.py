# app/main.py
from fastapi import FastAPI
from app.views import comment_router
from app.logging_config import setup_logging
from app.config import settings
from dotenv import load_dotenv

# Initialize logging when the application starts
setup_logging()

# Load environment variables from .env file
# This is important for loading sensitive information like API tokens
load_dotenv()

app = FastAPI()

# Include the comment routes
app.include_router(comment_router)