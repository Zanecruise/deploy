from fastapi import FastAPI
from .models import AvaliacaoRequest, AvaliacaoResponse
from .core import avaliar_carteira

app = FastAPI()

@app.post("/avaliar", response_model=AvaliacaoResponse)
async def avaliar(request: AvaliacaoRequest):
    score, risco = avaliar_carteira(request.carteira, request.evento, request.valor)
    return AvaliacaoResponse(
        carteira=request.carteira,
        risco=risco,
        score=score
    )
