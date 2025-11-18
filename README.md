# CivicPulse ML API

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

## Project Structure

```
CIVICPULSE-ML-DEV/
├── .git/
├── .venv/              # local dev environment
│
├── data/               # sample images for testing
│
├── models/             # model weights
│
├── notebooks/          # Jupyter notebooks for experiments
│
├── src/                # source code
│   └── main.py
│
├── tests/              # unit tests folder
│
├── .dockerignore       # required for docker builds
├── .gitignore
├── .python-version
├── Dockerfile          # docker configuration file
│
├── LICENSE
├── pyproject.toml      # uv dependency file
├── README.md
└── uv.lock
```

## Getting Started

## Installation & Setup

This project uses **uv** as the package and environment manager, along with a `pyproject.toml`–based dependency setup.

### **1. Install uv**

If you don’t have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### **2. Create & activate the environment**

```bash
uv venv
source .venv/bin/activate
```

### **3. Install dependencies**

```bash
uv sync
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

## Contributing

Feature branches and pull requests are welcome.
Please follow the repository’s issue templates and branching guidelines.

## License

_This project is part of the **CivicPulse** academic initiative formed by TIET students for their Software Engineering project.
For usage outside the project's academic scope, please contact the maintainers._

© 2025 CivicPulse Team. All rights reserved.
