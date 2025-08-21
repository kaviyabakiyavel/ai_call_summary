from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime
from .database import Base

class AudioTranscript(Base):
    __tablename__ = "audio_transcripts"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True, nullable=False)
    transcript = Column(String, nullable=False)
    summary = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
