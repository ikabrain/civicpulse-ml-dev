# src/civicpulseML/model.py

from functools import lru_cache
import json
from pathlib import Path

from civicpulseML.config import MODELS_DIR

_MODELS_METADATA_FILE = MODELS_DIR / "models_metadata.json"

# TODO: Add function save_model() to save/update metadata when new models are trained


@lru_cache(maxsize=1)
def _load_models_metadata() -> dict:
    """Load models metadata from JSON file."""
    if _MODELS_METADATA_FILE.exists():
        try:
            with open(_MODELS_METADATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


# TODO: Refactor to a more general get_model_weights_path(model_name: str) function if more models are added


def _get_yolo_weights_path() -> Path:
    """Get the path to YOLO weights from metadata, or discover it dynamically."""
    metadata = _load_models_metadata()

    # First, try to get from metadata file
    if "yolo" in metadata and "weights_path" in metadata["yolo"]:
        weights_path = Path(metadata["yolo"]["weights_path"])
        if weights_path.exists():
            return weights_path

    # Fallback: discover weights using naming convention
    expected_weights = (
        MODELS_DIR
        / "yolov8n-roboflow-license-plates"
        / "yolov8n_roboflow_license_plates_best.pt"
    )
    if expected_weights.exists():
        return expected_weights

    # If not found, raise helpful error
    raise FileNotFoundError(
        f"YOLO weights not found. Expected at: {expected_weights}\n"
        "Please train the model first using notebook 0.01-ika-roboflow-yolo.ipynb"
    )


# Module-level property for easy access
YOLO_WEIGHTS_PATH: Path = _get_yolo_weights_path()
