from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from app.database import SessionLocal
from app.models.user_model import User
from app.auth.auth_handler import signJWT

router = APIRouter()

# Use ARGON2 instead of bcrypt
pwd = CryptContext(schemes=["argon2"], deprecated="auto")

@router.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(400, "Email already exists")

    user = User(email=email, password=pwd.hash(password))
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd.verify(password, user.password):
        raise HTTPException(401, "Invalid credentials")
    return signJWT(user.id)
