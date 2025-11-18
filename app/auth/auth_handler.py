import time
from jose import jwt
from app.config import JWT_SECRET

def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 3600 * 24,  # 24 hours
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}

def decodeJWT(token: str):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        if decoded.get("expires", 0) >= time.time():
            return decoded
        return None
    except Exception:
        return None
