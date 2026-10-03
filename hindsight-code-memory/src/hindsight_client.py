from hindsight_client import Hindsight
from .config import HINDSIGHT_URL
import os

def get_client():
    # Supports both local and Hindsight Cloud
    url = os.getenv("HINDSIGHT_URL", HINDSIGHT_URL)
    return Hindsight(base_url=url)

def retain_memory(bank_id: str, content: str, context: str = "codebase"):
    client = get_client()
    # Key learning: retain as short factual sentence, not blob
    return client.retain(bank_id=bank_id, content=content, context=context)

def recall_memory(bank_id: str, query: str, k: int = 10):
    client = get_client()
    result = client.recall(bank_id=bank_id, query=query)
    # Return text + scores
    return result.results[:k]

def reflect_memory(bank_id: str, query: str):
    client = get_client()
    return client.reflect(bank_id=bank_id, query=query)
