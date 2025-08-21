from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from app.routers import audio

app = FastAPI()

# ✅ Allow all origins (for dev & frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "AI Call Summary Backend"}

# Routers
app.include_router(audio.router)
