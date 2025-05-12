from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from sqlalchemy import text

DATABASE_URL = "sqlite:///./call_summary.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False, "timeout":60})
SessionLocal = sessionmaker(bind=engine)

# Set journal_mode to WAL for better concurrency
with engine.connect() as conn:
    conn.execute(text("PRAGMA journal_mode=WAL"))

SessionLocal = sessionmaker(bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
