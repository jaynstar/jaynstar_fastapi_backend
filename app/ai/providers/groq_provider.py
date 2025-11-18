from groq import Groq
from app.config import GROQ_API_KEY

PROVIDER_NAME = "groq"

def is_available() -> bool:
    return bool(GROQ_API_KEY)

def generate_resume(details: str) -> str:
    if not is_available():
        raise ValueError("GROQ_API_KEY not set")

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
You are a professional Australian resume writer.
Write a clean, ATS-friendly resume in plain text.

User details:
{details}

Rules:
- No markdown
- No bullet points
- Plain text only
- Sections: SUMMARY, SKILLS, EXPERIENCE, EDUCATION
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
