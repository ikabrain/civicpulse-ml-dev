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

civicpulse-ml/
├── app/
│   ├── api/              # FastAPI routes
│   ├── core/             # Config & utilities
│   ├── ml/               # Models, preprocessing, inference
│   └── main.py           # Application entrypoint
├── models/               # Trained weights (ignored in Git)
├── requirements.txt
└── README.md

```

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API locally

```bash
uvicorn app.main:app --reload
```

### 3. Test OCR endpoint

```bash
curl -X POST -F "image=@car.jpg" http://localhost:8000/api/ocr/plate
```

## Contributing

Feature branches and pull requests are welcome.
Please follow the repository’s issue templates and branching guidelines.

## License

_This project is part of the **CivicPulse** academic initiative formed by TIET students for their Software Engineering project.
For usage outside the project's academic scope, please contact the maintainers._

© 2025 CivicPulse Team. All rights reserved.
