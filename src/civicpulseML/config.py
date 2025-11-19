import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env once
load_dotenv(override=False)

# --- Project Directories ---

# Project root (assuming this file is inside src/civicpulseML/)
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"
INTERIM_DIR = DATA_DIR / "interim"

MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"

# --- API Keys ---

ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
if ROBOFLOW_API_KEY is None:
    raise ValueError("ROBOFLOW_API_KEY not set in .env")
