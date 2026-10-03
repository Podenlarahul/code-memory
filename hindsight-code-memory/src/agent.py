from .hindsight_client import recall_memory, reflect_memory
from .config import BANK_ID
import os

SYSTEM_PROMPT = """You are CodeMemory, a codebase-aware assistant with persistent memory from Hindsight.

Use these memories from past sessions to answer accurately. If memories conflict, prioritize recent.

MEMORIES:
{memories}

MENTAL MODELS:
{models}
"""

def build_context(bank_id: str, question: str):
    recalls = recall_memory(bank_id, question, k=8)
    memories_text = "\n".join([f"- {r.text} (score: {r.scores.get('final',0):.2f})" for r in recalls])

    # Reflect for higher-level understanding
    models = ""
    try:
        for mq in ["What are project conventions?", "What are architecture decisions?"]:
            res = reflect_memory(bank_id, mq)
            models += f"\n{mq}: {res.text if hasattr(res,'text') else str(res)}\n"
    except:
        pass

    return SYSTEM_PROMPT.format(memories=memories_text, models=models)

def ask_agent(question: str, bank_id: str = BANK_ID):
    context = build_context(bank_id, question)
    print("=== RECALL USED ===")
    print(context[:2000])
    print("\n=== ANSWER ===")
    # Call Groq / OpenAI here
    # For hackathon demo, we return the context as proof of memory use
    # Replace with actual LLM call:
    # from groq import Groq; client = Groq(); completion = client.chat.completions.create(...)
    return f"Based on {bank_id} memories:\n{context}\n\nQuestion: {question}\n\n[Wire your LLM here - Groq openai/gpt-oss-120b recommended]"
