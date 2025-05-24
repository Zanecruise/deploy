from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import jwt

SECRET_KEY = "SEU_SECRET_FORTE_AQUI"
security = HTTPBearer()

def verificar_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token ausente.")
    try:
        token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido.")
