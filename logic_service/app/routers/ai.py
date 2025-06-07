from celery.bin.result import result
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.ai_logic import analyze_entry


router = APIRouter()

class AnalyzeRequest(BaseModel):
    content: str


@router.post("/analyze/")
def analyze(request: AnalyzeRequest):
    try:
        result = analyze_entry(request.content)
    except HTTPException:
        raise HTTPException(status_code=500, detail="error")

    return result
