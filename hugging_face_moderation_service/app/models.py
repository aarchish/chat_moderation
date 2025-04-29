# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    text: str
    flagged: Optional[bool] = False # Indicates if the comment is flagged : Default is False if not provided
    moderation_labels: Optional[List[str]] = []
