import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.environ.get("HF_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"
BASE_DIR = Path(__file__).resolve().parents[2]
DB_FAISS_PATH = BASE_DIR / "vectorstore" / "db_faiss"
DATA_PATH = BASE_DIR / "data"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
