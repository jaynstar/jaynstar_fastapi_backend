import requests
from app.config import HF_API_KEY

PROVIDER_NAME = "huggingface"

# Free, stable text model
MODEL_NAME = "google/flan-t5-large"


def is_available() -> bool:
    return bool(HF_API_KEY)


def generate_resume(details: str) -> str:
    if not is_available():
        raise ValueError("HF_API_KEY not set")

    prompt = f"""
You are a professional Australian resume writer.
Write a clean TEXT resume based on:

{details}

Rules:
- No markdown
- No bullets
- Include: SUMMARY, SKILLS, EXPERIENCE, EDUCATION
"""

    url = f"https://router.huggingface.co/hf-inference/models/{MODEL_NAME}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 600,
            "temperature": 0.4,
        },
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=60)

    if resp.status_code != 200:
        raise RuntimeError(f"HuggingFace error {resp.status_code}: {resp.text}")

    data = resp.json()

    # HF usually returns: [{"generated_text": "..."}]
    if isinstance(data, list) and data and "generated_text" in data[0]:
        return data[0]["generated_text"].strip()

    return str(data)
