import google.generativeai as genai
from app.config import GEMINI_API_KEY

PROVIDER_NAME = "gemini"


def is_available() -> bool:
    return bool(GEMINI_API_KEY)


def generate_resume(details: str) -> str:
    if not is_available():
        raise ValueError("GEMINI_API_KEY not set")

    genai.configure(api_key=GEMINI_API_KEY)

    prompt = f"""
Write a professional Australian resume in plain text.

User details:
{details}

Rules:
- No markdown
- No bullet points
- Sections: SUMMARY, SKILLS, EXPERIENCE, EDUCATION
"""

    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    resp = model.generate_content(prompt)

    return resp.text.strip()
