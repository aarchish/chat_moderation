# app/services.py

import logging

import httpx
from app.config import settings

# Set up logger
logger = logging.getLogger("app")

# Set up the Hugging Face API URL and token
# You can set the token in your environment variables or .env file
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
HUGGINGFACE_API_TOKEN = settings.HUGGINGFACE_API_TOKEN


async def moderate_text(text: str):
    logger.info(f"Received text for moderation: {text}")

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {"inputs": text}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                HUGGINGFACE_API_URL, headers=headers, json=payload
            )
            response.raise_for_status()
        except httpx.RequestError as e:
            logger.error(f"Error calling Hugging Face API: {e}")
            return {"error": "Failed to moderate text"}

    results = response.json()[0]  # Extract the first result
    # Flag if any label has a score above a threshold (e.g., 0.8)
    flagged_labels = [r["label"] for r in results if r["score"] > 0.8]

    logger.info(f"Moderation result: {flagged_labels}")

    return flagged_labels
