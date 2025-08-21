from pydantic import BaseModel
from datetime import datetime

# --------------------------
# Transcript Schemas
# --------------------------
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

# --------------------------
# Audio Transcript Schemas
# --------------------------
class AudioTranscriptCreate(BaseModel):
    filename: str
    transcript: str

class AudioTranscriptResponse(BaseModel):
    id: int
    filename: str
    transcript: str
    summary: str
    created_at: datetime

    class Config:
        from_attributes = True
