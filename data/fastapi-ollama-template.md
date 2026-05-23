# Project: fastapi-ollama-template

## Description

A minimal FastAPI template for building AI-powered backends using Ollama.

It is designed for:

- fast experimentation
- reusable prompt patterns
- iterative AI development

---

## Purpose

Building AI backends often involves:

- repeated setup work
- inconsistent prompt handling
- difficulty iterating on LLM behavior

This template provides a simple starting point to:

- build API-based AI tools quickly
- experiment with prompts
- evolve systems through real usage

---

## Key Idea

This is a **prompt-first backend template**.

Instead of focusing on architecture first, it emphasizes:

- rapid experimentation
- logging and feedback loops
- evolving prompts into production endpoints

👉 Not: “perfect system design”  
👉 But: “iterate and improve through usage”

---

## Features

- FastAPI backend skeleton
- Ollama integration (local LLMs)
- Prompt template system
- Prebuilt AI endpoints:
  - `/ai/generate` – generic generation
  - `/ai/summarize` – summarize text
  - `/ai/classify` – classify input
  - `/ai/extract` – extract structured data
  - `/ai/playground` – experiment freely
- JSONL logging of prompt/response interactions

---

## Input / Output

### Input

- API requests (text prompts or structured input)

### Output

- LLM-generated responses
- Structured outputs depending on endpoint
- Logged prompt/response pairs

---

## Example Usage

### Summarize

```

POST /ai/summarize
{
"prompt": "FastAPI is a modern, fast web framework for building APIs with Python."
}

```

---

### Playground

```

POST /ai/playground
{
"prompt": "Explain FastAPI like I'm 12"
}

```

---

## Architecture

Client (API request)
↓
FastAPI endpoint
↓
Prompt template (optional)
↓
Ollama (LLM)
↓
Response
↓
Logging (JSONL)

---

## Project Structure

```

app/
api/ # API endpoints
prompts/ # Prompt templates
schemas/ # Pydantic models
services/ # Ollama integration
utils/ # Logging utilities

logs/ # Prompt/response logs (gitignored)

```

---

## Prompt System

Prompts are reusable building blocks stored in:

```

app/prompts/

```

Each prompt:

- defines a template
- provides a builder function

This makes prompts:

- reusable
- testable
- easy to evolve

---

## Playground

The `/ai/playground` endpoint is used for exploration.

- no templates
- no strict structure
- raw input → response

Use it to:

- test ideas
- iterate on prompts
- debug LLM behavior

---

## Development Workflow

The system is designed around a feedback loop:

```

playground → logs → feedback → prompts → endpoints

```

Flow:

1. Experiment in `/ai/playground`
2. Review logs (`logs/ai_logs.jsonl`)
3. Capture insights (FEEDBACK.md)
4. Refine prompts into templates
5. Expose via structured API endpoints

---

## Logging

All interactions are stored locally:

```

logs/ai_logs.jsonl

```

Each entry includes:

- timestamp
- endpoint
- prompt
- response

This enables:

- prompt iteration
- debugging
- dataset creation

---

## Tech Stack

- Python
- FastAPI
- Ollama (local LLMs)
- Pydantic

---

## Scope

This template is intentionally minimal.

It does NOT:

- provide production-ready infrastructure
- include authentication or scaling
- enforce complex architecture

It is focused on:
👉 fast local experimentation with AI backends

---

## Usage

```

git clone <repo-url>
cd fastapi-ollama-template
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload

```

Open:

```

<http://localhost:8000/docs>

```

---

## Future Ideas

- Better prompt management
- Advanced logging pipelines
- Evaluation tooling
- Integration with external APIs
- Structured output validation

---

## Philosophy

- Minimal and fast to start
- Prompt-first development
- Learn through real usage
- Avoid overengineering
- Iterate based on feedback

---

## Project Docs

- `FEEDBACK.md` – prompt experiments and learnings
- `PROMPT_EVOLUTION.md` – how prompts evolve into templates

---

## Template Usage

This repository can be used as a starting point for new projects.

👉 Click **"Use this template"** on GitHub to create a copy.

---

## Requirements

- Python 3.10+
- Ollama running locally

---

## Notes

- Logs are ignored via `.gitignore`
- Optimized for local development
- Extend only when needed

---

## License

MIT
