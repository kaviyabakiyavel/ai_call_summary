from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Transcript(Base):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    transcript_text = Column(String)
    summary = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Commlog(Base):
    __tablename__ = "commlogs"
    id = Column(Integer, primary_key=True)
    transcript_id = Column(Integer, ForeignKey("transcripts.id"))
    inserted_at = Column(DateTime, default=datetime.utcnow)
