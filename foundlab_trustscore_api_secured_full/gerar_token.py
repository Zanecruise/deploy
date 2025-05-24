import jwt
import datetime

SECRET_KEY = "SEU_SECRET_FORTE_AQUI"

def gerar_token():
    payload = {
        "sub": "foundlab-user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print(token)

if __name__ == "__main__":
    gerar_token()
