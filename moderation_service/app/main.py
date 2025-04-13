# app/main.py

from fastapi import FastAPI
from app.views import comment_router
from app.logging_config import setup_logging
from app.config import settings

# Initialize logging when the application starts
setup_logging()

app = FastAPI()

# Include the comment routes
app.include_router(comment_router)
