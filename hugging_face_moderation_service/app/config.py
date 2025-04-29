# app/config.py

import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HUGGINGFACE_API_TOKEN: str
    PORT: int = 8001  # Default port if not provided in .env file
    HOST: str = "localhost"  # Default host if not provided in .env file

    class Config:
        env_file = os.path.join(
            os.path.dirname(__file__), "../.env"
        )  # Pointing to the root .env file


# Instantiate the settings object to use in your app
settings = Settings()
