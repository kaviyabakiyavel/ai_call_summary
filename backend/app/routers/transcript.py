from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from typing import List
import os
from dotenv import load_dotenv
from openai 

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_summary(transcript_text: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following transcript from a dental office phone call."},
                {"role": "user", "content": transcript_text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")

@router.post("/transcripts", response_model=schemas.TranscriptOut)
def create_transcript(payload: schemas.TranscriptCreate, db: Session = Depends(get_db)):
    # Just mock a summary for now
    # summary = "This is a mock summary."
    summary = generate_summary(payload.transcript_text)
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

@router.post("/summarize", response_model=schemas.SummaryResponse)
async def summarize_transcript(data: schemas.TranscriptRequest):
    summary = generate_summary(data.transcript)
    return {"summary": summary}