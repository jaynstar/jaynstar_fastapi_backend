from fastapi import APIRouter
from app.ai.ai_router import generate_resume_smart

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/cover_letter")
def generate_cover_letter(details: str):
    prompt = f"Write a professional Australian cover letter:\n\n{details}"
    result = generate_resume_smart(prompt)
    return {"result": result}


@router.post("/selection_criteria")
def generate_selection_criteria(details: str):
    prompt = f"Write a detailed Australian selection criteria response:\n\n{details}"
    result = generate_resume_sart(prompt)
    return {"result": result}
