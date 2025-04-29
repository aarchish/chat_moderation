# app/views.py
from fastapi import APIRouter, HTTPException
from app.models import Comment
from app.services import moderate_text
from pydantic import BaseModel

comment_router = APIRouter()

class ModerationResponse(BaseModel):
    flagged: bool
    labels: list[str]

@comment_router.post("/comment/")
async def create_comment(comment: Comment):
    try:
        flagged_labels = await moderate_text(comment.text)
        is_flagged = len(flagged_labels) > 0
        return ModerationResponse(flagged=is_flagged, labels=flagged_labels)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
