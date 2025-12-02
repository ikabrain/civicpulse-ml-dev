import os
from pathlib import Path

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

# --- Hardware Config ---

CUDA_AVAILABLE = os.getenv("CUDA_AVAILABLE", "False").lower() in ("true", "1", "t")
