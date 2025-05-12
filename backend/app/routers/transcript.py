from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from typing import List

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transcripts", response_model=schemas.TranscriptOut)
def mc(payload: schemas.TranscriptCreate, db: Session = Depends(get_db)):
    # Just mock a summary for now
    summary = "This is a mock summary."
    return crud.create_transcript(db, payload.transcript_text, summary)

@router.get("/transcripts", response_model=List[schemas.TranscriptOut])
def get_all_transcripts(db: Session = Depends(get_db)):
    return crud.get_transcripts(db)

@router.post("/commlog/{transcript_id}")
def create_commlog_entry(transcript_id: int, db: Session = Depends(get_db)):
    return crud.create_commlog(db, transcript_id)
    
@router.delete("/transcripts")
def delete_transcripts(db: Session = Depends(get_db)):
    return crud.delete_transcripts(db)

@router.delete("/commonlogs")
def delete_commlogs(db:Session = Depends(get_db)):
    return crud.delete_commlogs(db)