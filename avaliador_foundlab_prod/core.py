import openai
import pandas as pd
import re
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def call_ia_api(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message['content']

def extrair_nota_feedback(texto):
    nota_match = re.search(r"Nota:\s*([0-9]+(?:\.[0-9]+)?)", texto)
    nota = float(nota_match.group(1)) if nota_match else None
    feedback = texto.strip()
    return nota, feedback

def gerar_prompt_avaliacao(resposta_usuario):
    template_feedback = f"""Você é um copiloto estratégico que deve avaliar a resposta do founder com:

- Nota de 0 a 10
- Justificativa clara
- Identificação de riscos e fragilidades
- Sugestão de pelo menos uma melhoria ou alternativa
- Feedback direto e prático, sem suavizações

Resposta do founder:
{resposta_usuario}

Agora faça a avaliação:
"""
    return template_feedback
