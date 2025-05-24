# FoundLab TrustScore API

API de reputação comportamental baseada em carteiras digitais e eventos financeiros.

## Rota Principal

**POST** `/trustscore`

### Payload de entrada

```json
{
  "wallet": "0xA1B2C3",
  "evento": "mint",
  "valor": 250
}
```

### Resposta

```json
{
  "wallet": "0xA1B2C3",
  "evento": "mint",
  "valor": 250,
  "trustscore": 93,
  "decisao": "liberado",
  "tier": "muito confiável",
  "badge": "verde"
}
```

## Execução Local

```bash
uvicorn main:app --reload
```

## Docker

```bash
docker build -t foundlab-api .
docker run -p 8080:8080 foundlab-api
```

## Deploy recomendado

Google Cloud Run + API Gateway (com autenticação opcional via token JWT)
