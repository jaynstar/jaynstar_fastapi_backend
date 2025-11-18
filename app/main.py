from fastapi import FastAPI
from app.routes.doc_routes import router as doc_router
from app.routes.ai_routes import router as ai_router
from app.auth.routes import router as auth_router
from app.database import Base, engine
from app.auth.admin_routes import router as admin_router
from app import models   # <-- IMPORTANT: loads all models
from app.routes.cover_letter_routes import router as cover_router
app.include_router(cover_router)



# Create DB tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jaynstar Document API",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "Jaynstar FastAPI backend running!"}

# Attach route groups
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(doc_router, prefix="/docs", tags=["Documents"])
app.include_router(ai_router, prefix="/ai", tags=["AI"])
app.include_router(admin_router, prefix="/auth", tags=["Admin"])

