# projects-ai

A CLI tool that helps you **turn your past projects into new ideas** using local AI.

> Not just search.  
> Not just answers.  
> 👉 A tool for _thinking and deciding what to build next_

---

## 💡 Why this exists

I build many small tools and projects.

Over time, I forget:

- what I’ve already built
- patterns in how I build
- which ideas I’ve already explored

This tool turns my project READMEs into a:

👉 **thinking interface**

So instead of searching manually, I can ask:

```
projects-ai ask "What should I build next?"
projects-ai ask "What patterns am I repeating?"
projects-ai ask "What am I not exploring yet?"
```

---

## 🧠 What this actually does

- Loads project READMEs
- Uses RAG (LlamaIndex + Ollama)
- Generates structured, **high-signal outputs**

But the real value is not retrieval.

👉 The real value is:

- generating ideas
- extracting patterns
- helping me move forward

---

## 🔥 Core idea

This tool is designed for:

👉 **momentum**

Success is not:

- “did it answer correctly?”

Success is:

- Did I get a useful idea?
- Did it trigger action?
- Did it help me decide faster?

---

## 🧪 Example output

```
## Answer
Focus on tools that reduce decision friction in everyday workflows.

## Key Points
- Your projects consistently simplify complex inputs into fast decisions
- You prefer CLI-first, low-friction tools

## Suggestion
- decision-memory CLI: log decisions + reasoning → query later “why did I choose this?”
- ArticleLens: visualize article structure → quickly understand main ideas without reading everything
```

👉 Fast to read  
👉 Actionable  
👉 Meant to trigger thinking

---

## ⚙️ Tech stack

- Python
- LlamaIndex (RAG orchestration)
- Ollama (local LLMs)
- Markdown-based data

---

## 📂 Project structure

```
projects-ai/
  data/               # Project READMEs
  src/
    rag.py            # Index + query logic
    cli.py            # CLI interface
  README.md
```

---

## 🚀 Getting started

### 1. Add your data

Put project README files in:

```
./data/
```

Recommended structure:

```md
# Project: name

## Description

...

## Tech

...

## Key ideas

...
```

---

### 2. Install dependencies

```
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```

---

### 3. Start Ollama

```
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

---

### 4. Ask questions

```
projects-ai ask "What should I build next?"
```

---

## 🧠 How it works (simple)

```
CLI → RAG → Prompt → Structured output → Ideas
```

The key is not the architecture.

👉 The key is the **prompt + output design**

---

## 🔍 Key learnings so far

- Structured READMEs massively improve output quality
- Output format matters more than retrieval tweaks
- Short, dense answers > long explanations
- The best outputs:
  - are easy to scan
  - feel slightly surprising
  - trigger action

---

## ⚠️ Limitations

- RAG ≠ database
  - aggregation (counting/listing) is weak
- Insights are based only on README data
- Suggestions can still be:
  - safe
  - pattern-repeating (improving over time)

---

## 🧭 Current focus

Improving:

- ✅ output clarity (mostly solved)
- 🔄 idea quality (ongoing)
- 🔄 making suggestions more:
  - specific
  - personal
  - actionable

---

## 🔮 Future directions

- Include:
  - FEEDBACK.md
  - project context files
- Add:
  - better idea generation
  - stronger pattern extraction
- Possibly:
  - “first step” suggestions (micro-actions)

---

## 🚫 Non-goals

- Not a general knowledge base
- Not a production search system
- Not overengineered

Keep it:

👉 simple  
👉 fast  
👉 useful

---

## 🧠 What makes this interesting

This is not just:

- a RAG project
- a CLI tool

This is:

👉 a **personal thinking system**

A tool that helps turn:

```
past work → future direction
```

---

## ✅ Development philosophy

```
Ask → Observe → Log → Improve → Repeat
```

The most important thing is:

👉 real usage → real feedback

---

## 📄 License

MIT
