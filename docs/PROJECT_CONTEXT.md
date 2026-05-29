# projects-ai – Project Context

---

## 🧠 What this project is

projects-ai is a CLI tool that lets me ask questions about my own software projects using AI (RAG + local LLMs).

It turns my project READMEs into a:

👉 **thinking and idea-generation interface**

The goal is NOT just to retrieve information.  
The goal is:

👉 to generate **useful ideas and next actions based on past work**

---

## 🎯 Core philosophy

This project is about:

- reducing friction in thinking about my own work
- extracting patterns _only if they help decision-making_
- turning past projects into **forward momentum**

Success is NOT:

- “did it give an answer?”

Success is:

- Did it give me an idea I can build?
- Did it make me want to take action?
- Did it help me decide faster?

---

## 🔥 Key shift (important)

The project has evolved from:

```
RAG → answer → insight
```

To:

```
RAG → structured output → suggestions → action
```

This is a shift from:

👉 a query tool  
to  
👉 a **momentum engine**

---

## 🧪 Current state

The system currently works as:

```
CLI → RAG → Prompt → Structured output
```

Current output structure:

```
## Answer
(short directional statement)

## Key Points
(1–2 bullets that justify direction)

## Suggestion
(1–2 concise, concrete project ideas)
```

Each suggestion is:

```
- <name>: <what it does> → <why it matters>
```

Key constraints:

- Short, scannable output
- At least one idea should feel slightly surprising
- Ideas must be:
  - specific
  - buildable
  - not repetitions of past projects

---

## ✅ What is working well now

- Outputs are fast to read (high signal density)
- Suggestions feel:
  - relevant
  - sometimes genuinely interesting
- The system often triggers:
  👉 “I want to build something”

This is the most important success signal.

---

## ⚠️ Current limitations

- Suggestions can still be:
  - slightly safe
  - pattern-repeating
- Limited by:
  - README-only data
- RAG limitations:
  - weak aggregation (counting/listing)
  - incomplete coverage

---

## 🧠 Key learnings so far

### 1. Output design > retrieval improvements

Improving the prompt and structure created far more value than improving retrieval.

### 2. Verbosity = friction

Long explanations significantly reduce usefulness in a CLI context.

### 3. Structure enables thinking

A consistent format makes answers easier to:

- scan
- compare
- act on

### 4. Suggestions are the highest-value component

- “Insight” sections were low value → removed
- Suggestions create momentum → primary focus

### 5. Constraints drive quality

Adding constraints like:

- “no repetition”
- “must be surprising”

significantly improves output quality

---

## 🧭 Current focus

Focus is now on:

- improving idea quality (not structure)
- making suggestions:
  - more specific
  - more personal
  - more interesting
- maintaining:
  - minimal output
  - high signal density

---

## 🧱 What we are NOT optimizing right now

- Retrieval quality (good enough for now)
- Metadata layers
- Complex multi-step pipelines
- UI complexity

👉 Keep the system simple

---

## 🔮 Likely next evolution

### Better suggestions

- more opinionated
- more “this is actually worth building”

### Micro-action layer (possible)

- “first step” suggestions
- align with microsteps philosophy

### Expanded data sources

- FEEDBACK.md
- project context files
- personal notes

---

## 🚫 Non-goals

- Not a full knowledge base system
- Not a production-grade RAG system
- Not overengineered
- Not focused on completeness

Keep it:

👉 simple  
👉 fast  
👉 actionable

---

## 🧠 Why this matters (personally)

This tool helps me:

- turn past projects into new ideas
- avoid repeating the same patterns blindly
- build things I actually find interesting
- start faster (reduce friction to action)

It is both:

- a technical learning project
- a **personal thinking + action tool**

---

## 🔄 Feedback-driven development

The system evolves through:

```
Ask → Observe → Log → Improve → Repeat
```

The most important signal is:

👉 “Did this make me want to build something?”

---

## 🚀 What I want help with in new chats

- Improving idea quality (not verbosity)
- Making suggestions more:
  - surprising
  - specific
  - actionable
- Maintaining minimal output
- Iterating step-by-step based on real usage
- Avoiding overengineering at all costs

---

## 💡 How to use this in a new chat

When starting a new chat:

```
I’m working on this project:

[paste PROJECT_CONTEXT.md]

I want help improving it step-by-step without overengineering.

Let’s continue from here:
[describe current issue or goal]
```

---
