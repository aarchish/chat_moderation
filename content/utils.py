# content/utils.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def moderate_text(text):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": text}

    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    
    results = response.json()[0]  # it's a list within a list
    # Flag if any label has a score above a threshold (e.g., 0.8)
    flagged_labels = [r for r in results if r["score"] > 0.8]
    return flagged_labels
