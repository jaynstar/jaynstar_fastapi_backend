from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from app.database import SessionLocal
from app.models.admin_model import AdminUser
from app.models.user_model import User
from app.auth.auth_handler import signJWT
from app.auth.admin_bearer import AdminJWTBearer

router = APIRouter()
pwd = CryptContext(schemes=["argon2"], deprecated="auto")

# ----------------------------------------------
# 1. ADMIN REGISTER
# ----------------------------------------------
@router.post("/admin/register")
def admin_register(email: str, password: str):
    db = SessionLocal()
    existing = db.query(AdminUser).filter(AdminUser.email == email).first()
    if existing:
        raise HTTPException(400, "Admin email already exists")

    admin = AdminUser(email=email, password=pwd.hash(password))
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return {"message": "Admin created", "id": admin.id}


# ----------------------------------------------
# 2. ADMIN LOGIN
# ----------------------------------------------
@router.post("/admin/login")
def admin_login(email: str, password: str):
    db = SessionLocal()
    admin = db.query(AdminUser).filter(AdminUser.email == email).first()

    if not admin or not pwd.verify(password, admin.password):
        raise HTTPException(401, "Invalid admin credentials")

    return signJWT(admin.id)


# ----------------------------------------------
# 3. LIST ALL USERS (PROTECTED)
# ----------------------------------------------
@router.get("/admin/users", dependencies=[Depends(AdminJWTBearer())])
def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    return [
        {"id": u.id, "email": u.email}
        for u in users
    ]


# ----------------------------------------------
# 4. LIST ALL ADMINS (PROTECTED)
# ----------------------------------------------
@router.get("/admin/admins", dependencies=[Depends(AdminJWTBearer())])
def list_admins():
    db = SessionLocal()
    admins = db.query(AdminUser).all()
    return [
        {"id": a.id, "email": a.email}
        for a in admins
    ]


# ----------------------------------------------
# 5. DELETE USER (PROTECTED)
# ----------------------------------------------
@router.delete("/admin/user/{user_id}", dependencies=[Depends(AdminJWTBearer())])
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}


# ----------------------------------------------
# 6. DELETE ADMIN (PROTECTED)
# ----------------------------------------------
@router.delete("/admin/admin/{admin_id}", dependencies=[Depends(AdminJWTBearer())])
def delete_admin(admin_id: int):
    db = SessionLocal()
    admin = db.query(AdminUser).filter(AdminUser.id == admin_id).first()
    if not admin:
        raise HTTPException(404, "Admin not found")

    db.delete(admin)
    db.commit()
    return {"message": "Admin deleted"}
