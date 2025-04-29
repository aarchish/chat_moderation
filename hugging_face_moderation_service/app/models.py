# app/models.py
from typing import List, Optional

from pydantic import BaseModel


class Comment(BaseModel):
    text: str
    flagged: Optional[bool] = (
        False  # Indicates if the comment is flagged : Default is False if not provided
    )
    moderation_labels: Optional[List[str]] = []
