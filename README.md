# FoundLab FullStack + Orchestrator - Deploy Ready

This package contains the merged FullStack ScoreLab application and the Orchestrator components.

## Contents
- Backend API (FastAPI)
- Frontend dashboard
- Orchestrator modules
- Dockerfile for containerization
- requirements.txt for dependencies

## Running Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

## Docker Build & Run
```bash
docker build -t foundlab-fullstack-orchestrator .
docker run -p 8080:8080 foundlab-fullstack-orchestrator
```

## Deploy on Cloud Run
Follow standard Google Cloud Run deployment steps for Python/FastAPI:
```bash
gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/foundlab-fullstack-orchestrator
gcloud run deploy foundlab-fullstack-orchestrator \
    --image gcr.io/$(gcloud config get-value project)/foundlab-fullstack-orchestrator \
    --region southamerica-east1 \
    --platform managed \
    --allow-unauthenticated
```
