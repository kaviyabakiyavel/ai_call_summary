from sqlalchemy.orm import Session
from . import models

# ------------------------------
# Create a new transcript record
# ------------------------------

def create_audio_transcript(db: Session, filename: str, transcript: str, summary: str):
    existing = db.query(models.AudioTranscript).filter_by(filename=filename).first()
    if existing:
        return existing

    db_transcript = models.AudioTranscript(
        filename=filename,
        transcript=transcript,
        summary=summary
    )
    db.add(db_transcript)
    db.commit()
    db.refresh(db_transcript)
    return db_transcript

# ------------------------------
# Fetch transcripts
# ------------------------------

def get_audio_transcripts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AudioTranscript).offset(skip).limit(limit).all()

# ------------------------------
# Delete records
# ------------------------------

def delete_audio_transcripts(db: Session, batch_size: int = 50):
    while True:
        to_delete = db.query(models.AudioTranscript).limit(batch_size).all()
        if not to_delete:
            break
        for record in to_delete:
            db.delete(record)
        db.commit()
    return {"message": "All audio transcripts deleted"}
