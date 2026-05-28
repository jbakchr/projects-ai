# projects-ai – Project Context

## 🧠 What this project is

projects-ai is a CLI tool that lets me ask questions about my own software projects using AI (RAG + local LLMs).

It turns my project READMEs into a **queryable knowledge base**.

The goal is NOT just to retrieve information.  
The goal is:

👉 to generate **insights about how I build and think**

---

## 🎯 Core philosophy

This project focuses on:

- reducing friction in understanding my own work
- extracting patterns across projects
- turning past projects into usable insights

Success is NOT:

- “did it give an answer?”

Success is:

- Did I gain insight?
- Did I understand something new about my projects?
- Did it help me think or decide faster?

---

## 🧪 Current state

The system currently works as:

```

CLI → RAG → LLM → structured answer

```

Key characteristics:

- Uses structured project READMEs in `/data`
- Uses LlamaIndex + Ollama
- Answers both:
  - single-project questions
  - cross-project pattern questions
- Prompt-driven structure (not hardcoded logic)

---

## 🔍 Key insights so far

- Structure in README files greatly improves RAG quality
- Cross-project questions are where real value emerges
- Prompt design directly affects:
  - clarity
  - structure
  - usefulness of answers

Biggest limitation:

👉 RAG is not a database

- aggregation (count/list) is weak
- coverage is sometimes incomplete

---

## 🧭 Intended direction (high level)

The project evolves in layers:

```

Search → Answers → Structure → Insights → Reflection

```

The goal is NOT complexity  
The goal is:

- better insight density
- better thinking support
- more useful output

---

## 🧱 Near-term evolution ideas

## 1. Output quality (current focus)

- improve structure and scan-ability
- reduce verbosity → increase signal
- make outputs feel like “decision dashboards”

---

## 2. Retrieval improvements

- better multi-document coverage
- reduce missed relevant projects
- improve pattern extraction consistency

---

## 3. CLI UX

- spinner ✅ (already added)
- cleaner output formatting
- clearer visual hierarchy

---

## 🔄 Structural shift (important)

From:

```

RAG → answer

```

To:

```

RAG → structured answer → insight extraction → reflection

```

This is the shift from:

👉 a query tool  
to  
👉 a thinking interface

---

## 🔮 Future evolution

## Metadata layer

- add structured metadata to projects
- enable more precise querying

## Expanded data sources

- include FEEDBACK.md
- include personal notes / ideas
- include project context files

## Suggestion capability

- “what should I build next?”
- “what patterns am I repeating?”

---

## 🚫 Non-goals

- Not a full knowledge base system
- Not a production search engine
- Not a complex AI platform
- Not overengineered

Keep it:

👉 simple  
👉 personal  
👉 useful

---

## ✅ What makes this project interesting

This is not:

- just a RAG system
- just a CLI tool

This is:

👉 a system that helps me **understand my own work better**

It combines:

- retrieval
- synthesis
- reflection

---

## 🧠 Why this matters (personally)

This project helps me:

- see patterns in what I build
- understand my design philosophy
- make better decisions about future projects

It is both:

- a technical learning project
- a personal thinking tool

---

## 🔄 Feedback-driven development

This project evolves through:

```

Ask → Observe → Log (FEEDBACK.md) → Improve → Repeat

```

The most important file is:

👉 FEEDBACK.md

---

## 🚀 What I want help with in a new chat

- Improving answer quality (structure + insight density)
- Making outputs more useful and scannable
- Enhancing cross-project reasoning
- Keeping everything minimal (no overengineering)
- Iterating step-by-step based on real usage

---

# 💡 How to use this in a new chat

When starting a new chat, say:

I’m working on this project:

[paste PROJECT_CONTEXT.md]

I want help improving it step-by-step without overengineering.
Let’s continue from here:
[describe current issue or goal]
