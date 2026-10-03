import os
from dotenv import load_dotenv
load_dotenv()

HINDSIGHT_URL = os.getenv("HINDSIGHT_URL", "http://localhost:8888")
BANK_ID = os.getenv("BANK_ID", "my-codebase")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
