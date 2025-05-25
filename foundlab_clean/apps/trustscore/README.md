# 🛡️ FoundLab TrustScore API

API para cálculo e avaliação de *TrustScore* comportamental de carteiras, usada para avaliação de risco, compliance e tomada de decisão automatizada.

---

## 📂 Estrutura

apps/
  trustscore/
    README.md         ← este arquivo
    requirements.txt  ← dependências Python
    src/
      main.py         ← ponto de entrada FastAPI
      core.py         ← lógica principal de score
      models.py       ← modelos Pydantic e schemas

---

## 🚀 Como rodar localmente

Pré-requisitos:
- Python 3.9+
- pip atualizado
- (opcional) Poetry para gerenciamento avançado

1. Crie um ambiente virtual
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows

2. Instale as dependências
   pip install -r requirements.txt

3. Rode a aplicação FastAPI (usando Uvicorn)
   uvicorn src.main:app --reload

A API ficará disponível em:
http://127.0.0.1:8000

---

## 🧪 Testando a API

Use o Insomnia ou Postman para enviar uma requisição POST para:

POST /trustscore
Content-Type: application/json

{
  "wallet": "0x1234...",
  "evento": "mint",
  "valor": 1000.0
}

Resposta esperada:
{
  "wallet": "0x1234...",
  "evento": "mint",
  "valor": 1000.0,
  "trustscore": 98,
  "decisao": "liberado",
  "tier": "excelente",
  "badge": "verde-escuro"
}

---

## ⚙️ Organização dos arquivos

- main.py: Entrypoint da API e rotas.
- core.py: Funções e lógica de cálculo do TrustScore.
- models.py: Schemas e validações dos dados de entrada/saída.
