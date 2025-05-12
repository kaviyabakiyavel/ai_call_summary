from sqlalchemy.orm import Session
from app import models

def create_transcript(db: Session, transcript_text: str, summary: str):
    transcript = models.Transcript(transcript_text=transcript_text, summary=summary)
    db.add(transcript)
    db.commit()
    db.refresh(transcript)

    # To automatically insert into the commlog table whenever a transcript is created. no need a seperate function 
    commlog = models.Commlog(transcript_id=transcript.id)
    db.add(commlog)
    db.commit()
    db.refresh(commlog)

    return transcript

def get_transcripts(db: Session):
    return db.query(models.Transcript).all()

def delete_transcripts(db: Session):
    batch_size = 50  # Adjust as needed
    while True:
        to_delete = db.query(models.Transcript).limit(batch_size).all()
        if not to_delete:
            break
        for record in to_delete:
            db.delete(record)
        db.commit()

    return {"message": "All transcripts deleted"}

def delete_commlogs(db:Session):
    batch_size = 50
    while True:
        to_delete = db.query(models.Commlog).limit(batch_size).all()
        if not to_delete:
            break
        for record in to_delete:
            db.delete(record)
        db.commit()
    return{"message": "All commlog record deleted"}