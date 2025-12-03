> ⚠️ **NOTE: Repository archived as taking an indefinite break from this project.** However, if you found interest, feel free to contribute to our org at [CivicPulseTIET/civicpulse-ml](https://github.com/CivicPulse-TIET/civicpulse-ml/)

# CivicPulse ML API

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

The **CivicPulse ML API** is a lightweight machine learning microservice designed to process vehicle images and automatically extract license plate numbers using deep learning and OCR. This service powers the verification pipeline of the CivicPulse platform by providing fast, accurate, and API-accessible image analysis.

## Features

- Vehicle license plate detection using a deep learning model (YOLO-based)
- Optical Character Recognition (OCR) for extracting plate numbers
- REST API built with FastAPI
- Support for image uploads via file or URL
- Modular pipeline: preprocessing → detection → OCR → response
- Easy integration with the main CivicPulse backend

## Tech Stack

- **Python**
- **FastAPI**
- **YOLOv8 / Detection Model**
- **Tesseract / EasyOCR**
- **OpenCV**
- **Uvicorn**

## API Endpoints

| Method | Endpoint         | Description                             |
| ------ | ---------------- | --------------------------------------- |
| POST   | `/api/ocr/plate` | Detects license plate and extracts text |
| GET    | `/health`        | Service health check                    |

## Project Organisation

```
├── LICENSE             <- Open-source license if one is chosen
├── Makefile            <- Makefile with convenience commands like `make data` or `make train`
├── README.md           <- The top-level README for developers using this project.
├── data
│   ├── external        <- Data from third party sources.
│   ├── interim         <- Intermediate data that has been transformed.
│   ├── processed       <- The final, canonical data sets for modeling.
│   └── raw             <- The original, immutable data dump.
│
├── models              <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
│                          the creator's initials, and a short `-` delimited description, e.g.
│                          `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml      <- Project configuration file with package metadata for
│                          civicpulseML and configuration for tools like ruff, black, isort, uv, etc.
│
├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures         <- Generated graphics and figures to be used in reporting
│
├── src/                <- Source code for use in this project.
│   └── civicpulseML
│       │
│       ├── __init__.py             <- Makes civicpulseML a Python module
│       │
│       ├── config.py               <- Store useful variables and configuration
│       │
│       ├── dataset.py              <- Scripts to download or generate data
│       │
│       ├── features.py             <- Code to create features for modeling
│       │
│       ├── modeling
│       │   ├── __init__.py
│       │   ├── predict.py          <- Code to run model inference with trained models
│       │   └── train.py            <- Code to train models
│       │
│       └── plots.py                <- Code to create visualizations
│
├── tests/              <- Unit tests and other test code
│
├── .dockerignore       <- Required for docker builds
├── Dockerfile          <- Docker configuration file
│
├── .gitignore          <- Git ignore file
│
├── .python-version     <- Python version file
│
└── uv.lock             <- uv lock file for dependency management
```

## Getting Started

## Installation & Setup

This project uses **uv** as the package and environment manager, along with a `pyproject.toml`–based dependency setup.

### **1. Install uv**

If you don’t have `uv` installed, run the following command in project root:

```bash
make uv
```

### **2. Create & activate the environment**

```bash
make create_environment
source .venv/bin/activate
```

### **3. Install dependencies**

```bash
make requirements
```

## Running the API

Start the FastAPI server:

```bash
uv run fastapi dev src/app/main.py
```

Or manually with uv:

```bash
uv run python -m src.app.main
```

The API will be available at:

```
http://localhost:8000
```

To test the API endpoint, try

```bash
curl -X POST -F "image=@car.jpg" http://localhost:8000/api/ocr/plate
```

## Running with Docker

Build the image:

```bash
docker build -t civicpulse-ml:dev .
```

Run the container:

```bash
docker run -p 8000:8000 civicpulse-ml:dev
```

## Experimenting with notebooks

To work with Jupyter notebooks, first ensure you have the development dependencies installed:

```bash
make requirements-nb
```

## Contributing

Feature branches and pull requests are welcome.
Please follow the repository’s issue templates and branching guidelines.

## License

_This project is part of the **CivicPulse** academic initiative formed by TIET students for their Software Engineering project.
For usage outside the project's academic scope, please contact the maintainers._

© 2025 CivicPulse Team. All rights reserved.
