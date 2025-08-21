# ai_call_summary
Created project by using FastAPI, Sqlite3 , ReactJs , Docker 

Step By Step 

1) Set Up the Project Folder 
mkdir ai-call-summary
cd ai-call-summary

2) Create Backend (FastAPI)
    A. Set up a virtual environment 
        - python -m venv env
        - source env/bin/activate

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

7) (Optional) Use OpenAI for Summary
   
8) requirement.txt is required when we deploy 
   its needed to install all the packages 

9) Create Frontend (React + Tailwind)

10) Frontend Features
 - Textarea to paste transcript
 - Button to submit (calls backend)
 - Display Transcript and Summary
 - Use Axios or Fetch to call your backend API.

11) Step up Tailwind 
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


12) Dockerize the App 
 Create a Dockerfile for backend and frontend separately, or use Docker Compose for both.

13) Deploy 
   - Render
   - Railway
   - Replit
   - DockerHub + VPS

14) README File for FE, BE



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


What is LLM ? 

LLM stands for Large Language Model — a type of AI model trained on huge amounts of text data to understand and generate human-like language.Popular LLMs include:
 - OpenAI GPT-3.5 / GPT-4 / GPT-4o
 - Google Gemini
 - Anthropic Claude
 - Meta LLaMA
 - Hugging Face models like BART, T5, or Falcon

 response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    temperature=0.5,
    messages=[
        {"role": "system", "content": "Summarize the following transcript..."},
        {"role": "user", "content": transcript_text}
    ]
)

Your range 0.5 to 0.7 is common and often used for balanced responses.

Temperature     Behavior
0.0             Deterministic, most predictable. Always gives the same answer. Good for facts.
0.5             Some creativity, but still focused. Good for summarization, support bots.
0.7             Balanced randomness — mixes creativity with logic. Default for ChatGPT.
1.0             Creative and diverse, more variation in responses.
>1.2            Very random, may generate less coherent answers.

Prompt Engineering Methods
1) Zero-shot Prompting
2) One-shot Prompting
3) Few-shot Prompting
4) Chain of Thought Prompting (CoT)
5) Self-Consistency Prompting
6) Role Prompting
7) Instruction Prompting
8) Multimodal Prompting (for GPT-4-turbo or GPT-4o)
9) ReAct Prompting (Reason + Act)
10) Context-aware Prompting

My project using this prompting technices 
Zero-shot prompting	
   You provide no examples of how the summary should look — the model infers the format and structure from the task itself.

Role prompting
	Your system message — “Summarize the following transcript from a dental office phone call” — gives the model context and purpose, which helps it behave like a virtual assistant for dental staff.

Now updated project from manual text to audio 
user can upload audio file by using whisper mode converts audio to text 