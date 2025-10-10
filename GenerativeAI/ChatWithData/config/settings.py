import os

from dotenv import load_dotenv

# Load .env file once
load_dotenv()

# API keys & settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DB_PATH = "data/data.db"
LLM_MODEL = "llama-3.1-8b-instant"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)
