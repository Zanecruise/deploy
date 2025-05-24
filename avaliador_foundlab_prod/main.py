import pandas as pd
from core import call_ia_api, extrair_nota_feedback, gerar_prompt_avaliacao
from datetime import datetime

def avaliar_respostas(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    resultados = []

    for idx, row in df.iterrows():
        resposta = str(row.get('resposta', '')).strip()
        if not resposta:
            print(f"[{row['id']}] Resposta vazia, pulando...")
            continue
        prompt_avaliacao = gerar_prompt_avaliacao(resposta)
        try:
            avaliacao = call_ia_api(prompt_avaliacao)
            nota, feedback = extrair_nota_feedback(avaliacao)
        except Exception as e:
            print(f"[{row['id']}] ERRO: {str(e)}")
            nota, feedback = None, f"Erro: {str(e)}"
        resultados.append({
            "id": row['id'],
            "resposta": resposta,
            "nota": nota,
            "feedback": feedback,
            "avaliado_em": datetime.utcnow().isoformat()
        })
        print(f"[{row['id']}] Avaliado com nota {nota}")

    df_result = pd.DataFrame(resultados)
    df_result.to_csv(output_csv, index=False)
    print(f"Avaliações salvas em {output_csv}")

if __name__ == "__main__":
    avaliar_respostas("data/respostas_usuario.csv", "data/avaliacoes_consolidadas.csv")
