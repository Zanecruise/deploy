#!/bin/bash

# Configurações iniciais
PROJECT_ID="foundlab-core-460315"
REGION="us-central1"
SERVICE_NAME="foundlab-api"
SECRET_KEY="INSIRA_SEU_SECRET_AQUI"

echo "Ativando projeto GCP: $PROJECT_ID"
gcloud config set project $PROJECT_ID

echo "Ativando APIs necessárias..."
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

echo "Criando arquivo .env"
echo "SECRET_KEY=$SECRET_KEY" > .env

echo "Criando Docker image e deploy para Cloud Run..."
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

gcloud run deploy $SERVICE_NAME   --image gcr.io/$PROJECT_ID/$SERVICE_NAME   --region $REGION   --platform managed   --allow-unauthenticated   --port 8080   --set-env-vars SECRET_KEY=$SECRET_KEY

echo "Deploy completo!"
gcloud run services describe $SERVICE_NAME --region $REGION --format 'value(status.url)'
