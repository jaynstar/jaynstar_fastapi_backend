from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from app.auth.auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        token = credentials.credentials
        decoded = decodeJWT(token)
        if not decoded:
            raise HTTPException(status_code=403, detail="Invalid or expired token")
        return decoded
