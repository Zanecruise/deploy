from pydantic import BaseModel

class Evento(BaseModel):
    wallet: str
    evento: str
    valor: float
