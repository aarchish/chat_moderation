# content/utils.py

import requests
from backend import utils

MODERATION_API_URL = utils.MODERATION_API_URL

def moderate_text(text: str):
    try:
        response = requests.post(MODERATION_API_URL, json={"text": text})
        response.raise_for_status()
        return response.json()  # Assuming the response is a JSON object with "flagged" and "labels" keys
    except requests.RequestException as e:
        # Log the exception or return empty list if error occurs
        print(f"Moderation service error: {e}")
        return {"flagged": False, "labels": []}  # return fallback dict