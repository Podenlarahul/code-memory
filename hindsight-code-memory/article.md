# I Built a Coding Agent That Actually Remembers My Codebase

Every Claude Code session starts from zero. Every Cursor chat forgets my architecture. I got tired of re-explaining my own project.

So I built CodeMemory — a codebase agent with Hindsight that learns.

## What it does
CodeMemory indexes any code folder into a Hindsight bank. Each file becomes a factual memory: "File middleware/auth.ts handles JWT refresh".

When I ask "Where do we handle payment failures?" it doesn't grep. It recalls.

## The core insight: typed facts, not blobs

My first version retained entire files. Recall was noisy.

The fix:
```python
def file_to_fact(path):
    return f"File {rel} contains: {preview}... Key exports from this file."
client.retain(bank_id=bank, content=fact, context=f"file:{rel}")
```

Short factual sentences produced 3x cleaner recall.

I also added mental models via Hindsight's reflect:
- What are project conventions?
- What architecture decisions were made?
- What does the developer prefer?

## Before / After

**Before (no memory):**
Q: "What auth pattern do we use?"
A: "I need to see your code."

**After (with Hindsight):**
Recall returns 8 memories including `middleware/auth.ts handles JWT with refresh token rotation, implemented after INC-8821`.
A: "You use JWT with refresh rotation in middleware/auth.ts, following the fix for INC-8821."

Same question. Different agent. Because it remembers.

## Stack
Hindsight Cloud (MEMHACK99 credits), hindsight-client Python SDK, Groq gpt-oss-120b, Streamlit for demo. The Hindsight GitHub repository and Hindsight docs made setup trivial. The Vectorize agent memory page explains why this matters beyond RAG.

## Lessons
1. Retain as facts, not files
2. Scope banks per-project-tagged so global preferences travel
3. Debounce retains, auto-recall on first turn
4. Test memory layer independently — was it Hindsight or my prompt?

Full code: [Your Repo] | Hindsight: https://github.com/vectorize-io/hindsight
