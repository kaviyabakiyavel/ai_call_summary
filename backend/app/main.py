from fastapi import FastAPI
from app.routers import transcript
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Call Summary Backend"}

app.include_router(transcript.router)