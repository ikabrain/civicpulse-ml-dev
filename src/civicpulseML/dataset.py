# src/civicpulseML/dataset.py

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from roboflow import Roboflow

from civicpulseML.config import RAW_DIR

# Load .env once
load_dotenv(override=False)


def _load_roboflow_api_key() -> str:
    """Load the Roboflow API key from environment variables."""
    api_key = os.getenv("ROBOFLOW_API_KEY")
    if api_key is None:
        raise ValueError("ROBOFLOW_API_KEY not set in .env")
    return api_key


def download_roboflow_dataset(
    workspace: str,
    project_name: str,
    version: int,
    format_type: str = "yolov11",
    output_dir: Optional[Path] = None,
) -> object:
    """
    Download the license plate recognition dataset from Roboflow.

    Parameters
    ----------
    workspace : str
        Roboflow workspace name
    project_name : str
        Roboflow project name
    version : int
        Dataset version number
    format_type : str
        Dataset format (default: "yolov11")
    output_dir : Path, optional
        Directory to save the dataset. If None, uses RAW_DIR / roboflow-project-name

    Returns
    -------
    Dataset object from Roboflow
    """
    if output_dir is None:
        output_dir = RAW_DIR / f"roboflow-{project_name}"
    output_dir.mkdir(parents=True, exist_ok=True)

    ROBOFLOW_API_KEY = _load_roboflow_api_key()

    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    project = rf.workspace(workspace).project(project_name)
    dataset_version = project.version(version)
    dataset = dataset_version.download(format_type, location=str(output_dir))

    return dataset
