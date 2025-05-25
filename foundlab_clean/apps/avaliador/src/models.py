from pydantic import BaseModel

class AvaliacaoRequest(BaseModel):
    carteira: str
    evento: str
    valor: float

class AvaliacaoResponse(BaseModel):
    carteira: str
    risco: str
    score: float
