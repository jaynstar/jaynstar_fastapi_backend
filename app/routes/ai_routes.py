from fastapi import APIRouter, HTTPException
from app.ai.ai_router import generate_resume_smart

router = APIRouter()

@router.post("/resume")
def get_ai_resume(details: str):
    """
    Generate a professional resume using a smart AI router.

    Order of providers:
    1) Groq
    2) HuggingFace
    3) Google Gemini
    4) OpenAI (last resort)
    """
    if not details or details.strip() == "":
        raise HTTPException(status_code=400, detail="Details text is required.")

    try:
        resume_text = generate_resume_smart(details)
        return {"resume": resume_text}
    except Exception as e:
        # Send high-level error message back
        raise HTTPException(
            status_code=500,
            detail=f"AI resume generation failed: {e}",
        )
