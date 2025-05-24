# Avaliador FoundLab

Sistema local para avaliação automatizada de respostas com base na IA da OpenAI.

## Como usar

1. Renomeie `.env.example` para `.env` e insira sua chave de API OpenAI.
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Coloque seu CSV de entrada na pasta `data/` com a coluna `resposta` e `id`.
4. Rode o script:
   ```
   python main.py
   ```

Resultado será salvo em `data/avaliacoes_consolidadas.csv`.

---

**Formato esperado do CSV de entrada:**

| id | resposta |
|----|----------|
| 1  | A resposta do founder vai aqui... |
