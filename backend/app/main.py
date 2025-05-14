from fastapi import FastAPI
from app.routers import transcript
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow frontend URLs (Render + local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-call-summary-frontend.onrender.com",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Call Summary Backend"}

app.include_router(transcript.router)
