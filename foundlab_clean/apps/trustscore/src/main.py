from fastapi import FastAPI
from .models import Evento
from .core import calcular_trustscore_comportamental, interpretar_score

app = FastAPI()

@app.post("/trustscore")
async def trustscore(evento: Evento):
    historico_wallet = {
        "negados": 2,
        "liberados": 6,
        "mudanca_comportamento": True,
        "eventos_dia": 3,
        "nft_foundlab": True,
        "flag_fraude": False,
        "apenas_mint": False,
        "trusted_origin": True,
        "curva_valor": "ascendente",
        "dormencia": False,
        "eventos_premium": 1,
        "dias_atividade": 10,
        "whitelisted": True
    }
    score = calcular_trustscore_comportamental(evento.wallet, evento.evento, evento.valor, historico_wallet)
    decisao, tier, badge = interpretar_score(score)
    return {
        "wallet": evento.wallet,
        "evento": evento.evento,
        "valor": evento.valor,
        "trustscore": score,
        "decisao": decisao,
        "tier": tier,
        "badge": badge
    }
