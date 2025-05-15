from pydantic import BaseModel
from datetime import datetime

class TranscriptCreate(BaseModel):
    transcript_text: str

class TranscriptOut(BaseModel):
    id: int
    transcript_text: str
    summary: str
    created_at: datetime

    class Config:
        from_attributes = True

class TranscriptRequest(BaseModel):
    transcript: str

class SummaryResponse(BaseModel):
    summary: str