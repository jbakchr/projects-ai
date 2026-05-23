# projects-ai

A simple CLI tool that lets you **ask questions about your own projects** using local AI (Ollama) + RAG.

---

## 💡 Why this exists

I build a lot of small tools and projects. Over time, I forget:

- What each project actually does
- Patterns in what I build
- Ideas I’ve already explored

This tool turns my past projects (README files) into a **queryable knowledge base**.

Instead of searching manually, I can ask:

```bash
projects-ai ask "What is microsteps-ai about?"
projects-ai ask "What kind of tools do I tend to build?"
projects-ai ask "What should I build next based on my past projects?"
```

---

## 🧠 What it does

- Loads project README files
- Builds a vector index (RAG)
- Uses a local LLM (Ollama)
- Answers questions based on your own data

👉 Think of it as:  
**"Search + reflection engine for your personal projects"**

---

## ⚙️ Tech stack

- Python
- LlamaIndex (RAG orchestration)
- Ollama (local LLM)
- Markdown (data source)

---

## 📂 Project structure

```
projects-ai/
  data/                # Your project README files
    microsteps-ai.md
    drdk-ai-summarizer.md

  src/
    rag.py             # RAG setup and query logic
    cli.py             # CLI interface

  README.md
```

---

## 🚀 Getting started

### 1. Add your data

Put your project README files into:

```
./data/
```

Example:

- `microsteps-ai.md`
- `drdk-ai-summarizer.md`

Each file should ideally include:

```markdown
# Project: microsteps-ai

## Description

...

## Tech

...

## Key ideas

...
```

---

### 2. Install dependencies

```bash
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```

---

### 3. Start Ollama

Make sure you have:

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

---

### 4. Run the CLI

```bash
projects-ai ask "What is microsteps-ai about?"
```

---

## 🧪 Example questions

General:

- "What projects have I built?"
- "What kind of tools do I tend to create?"

Specific:

- "What is microsteps-ai about?"
- "Which projects use Python?"

Reflective (🔥 best use case):

- "What should I build next?"
- "What patterns are common across my projects?"

---

## ⚠️ Known limitations

This project is intentionally simple.

RAG is:

- ✅ Good at summarizing and reasoning
- ⚠️ Less reliable for exact counting or listing

Example:

- "What is X about?" → great ✅
- "How many projects do I have?" → less reliable ⚠️

This is part of the learning.

---

## 🗺️ Roadmap

### ✅ V1 (current)

- `projects-ai ask "..."`

### 🔜 V2

- `projects-ai list` → list project names
- `projects-ai count` → count projects
- `projects-ai suggest` → better idea generation

### 🔮 Future ideas

- Metadata (tech, status, type)
- Better prompts
- CLI UX improvements (colors, formatting)
- Integration with real GitHub repos

---

## 🎯 Purpose of this project

This is both:

1. A **learning project** for understanding RAG systems
2. A **practical tool** for reflecting on past work

---

## 🧠 Key insight

This project helps answer:

> "What can I learn from the things I've already built?"

---

## 📄 License

MIT
