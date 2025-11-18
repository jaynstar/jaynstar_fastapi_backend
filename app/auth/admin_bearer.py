from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from app.auth.auth_handler import decodeJWT
from app.database import SessionLocal
from app.models.admin_model import AdminUser

class AdminJWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        token = credentials.credentials
        decoded = decodeJWT(token)

        if not decoded:
            raise HTTPException(status_code=403, detail="Invalid or expired token")

        db = SessionLocal()
        admin = db.query(AdminUser).filter(AdminUser.id == decoded["user_id"]).first()
        if not admin:
            raise HTTPException(status_code=403, detail="Admin access required")

        return decoded
