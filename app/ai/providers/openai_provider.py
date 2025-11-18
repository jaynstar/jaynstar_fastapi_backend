from openai import OpenAI
from app.config import OPENAI_API_KEY

PROVIDER_NAME = "openai"


def is_available() -> bool:
    return bool(OPENAI_API_KEY)


def generate_resume(details: str) -> str:
    if not is_available():
        raise ValueError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
You are a professional Australian resume writer.
Write a clean text resume.

Details:
{details}

Rules:
- No markdown
- No bullets
- Sections: SUMMARY, SKILLS, EXPERIENCE, EDUCATION
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900,
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()
