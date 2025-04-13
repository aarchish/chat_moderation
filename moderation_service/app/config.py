# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HUGGINGFACE_API_TOKEN: str
    PORT: int = 8001 # Default port if not provided in .env file

    class Config:
        env_file = ".env"

settings = Settings()
