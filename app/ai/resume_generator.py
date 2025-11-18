from openai import OpenAI
from app.config import OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_resume_from_details(details: str) -> str:
    prompt = f"""
You are a professional Australian resume writer.

Create a polished, ATS-friendly resume in plain text (NO bullet symbols, NO markdown),
based on these raw details:

{details}

Requirements:
- Australian spelling
- Sections: SUMMARY, KEY SKILLS, WORK EXPERIENCE, EDUCATION
- Plain text only (no '*', no '-', no Markdown)
- Easy to copy into Microsoft Word
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=900,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
