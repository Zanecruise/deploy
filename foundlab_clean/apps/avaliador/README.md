# Avaliador FoundLab

API simples para avaliação de risco de carteiras/eventos.

==================================
REQUISITOS

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

==================================
INSTALAÇÃO

1. Navegue até a pasta do avaliador:
   cd apps/avaliador

2. Instale as dependências:
   pip install -r requirements.txt

==================================
COMO EXECUTAR

Execute o servidor local:
   uvicorn src.main:app --reload

O servidor irá rodar em:
   http://127.0.0.1:8000

==================================
EXEMPLO DE REQUEST

Faça uma requisição POST para /avaliar com o seguinte JSON:

{
  "carteira": "0xabc123",
  "evento": "withdraw",
  "valor": 980
}

==================================
EXEMPLO DE RESPOSTA

{
  "carteira": "0xabc123",
  "risco": "moderado",
  "score": 55
}

==================================
ESTRUTURA DOS ARQUIVOS

- src/
    - main.py        (API FastAPI)
    - core.py        (Lógica de avaliação)
    - models.py      (Modelos Pydantic)
- requirements.txt   (Dependências)
- README.md   (este arquivo)

==================================
