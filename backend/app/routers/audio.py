import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from openai import OpenAI
from .. import crud, schemas, database
import uuid

router = APIRouter()
UPLOAD_FOLDER = "backend/app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load .env and OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-audio/", response_model=schemas.AudioTranscriptResponse)
async def upload_audio(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith((".mp3", ".wav", ".m4a")):
        raise HTTPException(status_code=400, detail="Invalid file type.")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Whisper transcription
        with open(filepath, "rb") as f:
            transcript_resp = client.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )
        transcript_text = transcript_resp.text

        # GPT summary
        summary_resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize this audio:\n\n{transcript_text}"}]
        )
        summary_text = summary_resp.choices[0].message.content

        # Save to DB with unique filename
        unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
        db_transcript = crud.create_audio_transcript(
            db=db,
            filename=unique_filename,
            transcript=transcript_text,
            summary=summary_text
        )

        return db_transcript

    finally:
        os.remove(filepath)
