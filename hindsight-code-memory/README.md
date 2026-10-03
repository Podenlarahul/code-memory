# CodeMemory — AI Agent That Learns Your Codebase Using Hindsight

Stateless coding agents forget your project after every session. CodeMemory gives them persistent memory that learns.

**Flow:** `Codebase Scan → Retain Facts → Ask Question → Recall → Reflect → Answer with Context`

## Quick Start
```bash
# 1. Start Hindsight
export OPENAI_API_KEY=sk-xxx
docker run -it -p 8888:8888 -p 9999:9999 -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY -v hindsight-data:/home/hindsight/.pg0 ghcr.io/vectorize-io/hindsight:latest

# 2. Install
pip install -r requirements.txt
cp .env.example .env # add your HINDSIGHT_URL and API_KEY

# 3. Index your code folder
python src/cli.py index ../your-project --bank my-codebase

# 4. Ask
python src/cli.py ask "What is our auth pattern?" --bank my-codebase
python src/cli.py ask "Where do we handle payment failures?" --bank my-codebase
```

## Why Hindsight?
- **Retain:** Stores facts like "Auth uses JWT with refresh in middleware/auth.ts"
- **Recall:** Finds relevant files/memories for any question
- **Reflect:** Builds mental models: Project Conventions, Architecture Decisions, User Preferences

Built with: Hindsight Cloud / Open Source + Groq / OpenAI

Links:
- Hindsight GitHub: https://github.com/vectorize-io/hindsight
- Hindsight Docs: https://hindsight.vectorize.io/
- Agent Memory: https://vectorize.io/what-is-agent-memory
