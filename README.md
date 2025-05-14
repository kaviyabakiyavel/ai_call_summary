# ai_call_summary
Created project by using FastAPI, Sqlite3 , ReactJs , Docker 

Step By Step 

1) Set Up the Project Folder 
mkdir ai-call-summary
cd ai-call-summary

2) Create Backend (FastAPI)
    A. Set up a virtual environment 
        - python -m venv env
        - env/Scripts/activate

    B. Install Dependencies 
        - pip install fastapi uvicorn sqlalchemy pydantic alembic sqlite3 openai

    C. Create main.py

    D. Start the server command
        - uvicorn app.main:app --reload

3) Create Database Models 
   Create models.py

4) Create Database Connection
   database.py

5) Create APIs
    - POST /transcripts: Accept transcript, generate summary (mock or real), save both
    - GET /transcripts: List all
    - Delete all Transcript API
    - POST /commlog/{transcript_id}: Create commlog for a transcript
    - Delete all commlogs API

6) Check all APIs working in live server and local DB 
   Liver Server URL - http://127.0.0.1:8000/docs
   Local DB - DB Browser for SQLite -> open call_summary.db -> click on browser data 

6) Create Frontend (React + Tailwind)

7) Frontend Features
 - Textarea to paste transcript
 - Button to submit (calls backend)
 - Display Transcript and Summary
 - Use Axios or Fetch to call your backend API.

 8) Step up Tailwind 
 - npm uninstall tailwindcss
 - npm install -D tailwindcss@3.4.1 postcss autoprefixer
 - npx tailwindcss init -p
 - Create postcss.config.js
 - Create tailwind.config.js
 - Create src/index.css
 - Clean Cache PowerShell
 - Remove-Item -Recurse -Force node_modules
 - Remove-Item -Force package-lock.json
 - npm install


 9) (Optional) Use OpenAI for Summary

 10) Dockerize the App 
 Create a Dockerfile for backend and frontend separately, or use Docker Compose for both.

 11) Deploy 
   - Render
   - Railway
   - Replit
   - DockerHub + VPS

13) README File for FE, BE



Project 
ai-call-summary/
│
├── app/
│   ├── main.py          # ✅ Your FastAPI entry point
│   ├── models.py        # Database models (Transcript, Commlog)
│   ├── schemas.py       # Request/response models using Pydantic
│   ├── database.py      # DB connection & setup
│   ├── crud.py          # Functions to handle DB logic
│   └── routers/
│       └── transcript.py  # API routes (modular)
│
├── requirements.txt     # Python dependencies , helps for developer to install all depdencies , helps Docker deployment , CI/CD pipeline 
├── README.md            # Project overview
└── .env                 # Environment variables (e.g., OpenAI key)
