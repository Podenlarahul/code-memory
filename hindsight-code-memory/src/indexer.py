import pathlib
from .hindsight_client import retain_memory

IGNORE_DIRS = {'.git','node_modules','dist','build','.next','__pycache__','venv','.venv'}
CODE_EXTS = {'.ts','.tsx','.js','.jsx','.py','.go','.java','.rs','.md','.json'}

def should_index(path: pathlib.Path):
    if any(d in path.parts for d in IGNORE_DIRS):
        return False
    return path.suffix in CODE_EXTS and path.stat().st_size < 200_000

def file_to_fact(file_path: pathlib.Path, root: pathlib.Path) -> str:
    rel = file_path.relative_to(root)
    try:
        content = file_path.read_text()[:4000]
    except:
        return ""
    # Convert to factual statement - critical for good recall
    preview = content[:600].replace("\n"," ")
    return f"File {rel} contains: {preview}... Key exports and patterns from this file."

def index_folder(root_path: str, bank_id: str):
    root = pathlib.Path(root_path).resolve()
    print(f"Indexing {root} into bank {bank_id}")
    count = 0
    for p in root.rglob("*"):
        if p.is_file() and should_index(p):
            fact = file_to_fact(p, root)
            if fact:
                retain_memory(bank_id, fact, context=f"file:{p.relative_to(root)}")
                count += 1
                if count % 20 == 0:
                    print(f"Retained {count} files...")
    print(f"Done. Retained {count} memories.")
    # Seed mental models
    from .hindsight_client import get_client
    client = get_client()
    seeds = [
        ("What are this project's conventions for code style, build, testing?", "project-conventions"),
        ("What durable architectural decisions were made and why?", "project-decisions"),
        ("What does the developer prefer in tooling and communication?", "user-preferences")
    ]
    for q, name in seeds:
        try:
            client.reflect(bank_id=bank_id, query=q)
            print(f"Seeded mental model: {name}")
        except Exception as e:
            print(f"Seed {name} skipped: {e}")
