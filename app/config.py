import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# AI Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
HF_API_KEY = os.getenv("HF_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Auth key
JWT_SECRET = os.getenv("JWT_SECRET", "CHANGE_ME_JWT_SECRET")
