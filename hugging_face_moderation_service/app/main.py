# app/main.py

# from app.config import settings
from app.logging_config import setup_logging
from app.views import comment_router
from fastapi import FastAPI

# Initialize logging when the application starts
setup_logging()

app = FastAPI()

# Include the comment routes
app.include_router(comment_router)
