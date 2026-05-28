# ROADMAP.md

## 🎯 Vision

projects-ai is a CLI tool that turns your past projects into a **queryable knowledge base**.

The long-term goal is:

👉 Turn scattered projects into **structured insight about how you think, build, and decide**

---

## 🧠 Core Idea

This is not just a RAG demo.

It is a tool for:

- understanding your own work
- identifying patterns across projects
- generating insights from past decisions

👉 A “thinking interface” over your own projects

---

# 🚀 Development Philosophy

- Start simple → evolve gradually  
- Favor real usage over theoretical design  
- Improve through feedback (`FEEDBACK.md`)  
- Avoid overengineering  

---

# ✅ Current State (V1)

### Working features

- CLI interface:
```

projects-ai ask "..."

````

- RAG over structured project READMEs

- Cross-project reasoning:
- Identify relevant projects
- Extract shared patterns
- Suggest developer tendencies

- Basic structured output:
- Relevant projects
- Shared patterns
- Developer insights

---

# 🔜 Next Steps (V2 — Output Quality & UX)

## 🎯 Goal
Make answers **more useful, scannable, and insight-dense**

### Improvements

- Better output structure (clean sections)
- Consistent formatting (bullets, hierarchy)
- Reduce verbosity → increase signal
- Improve pattern specificity (less generic LLM phrasing)

---

## 🖥️ CLI UX Improvements

- Spinner (✅ done)
- Cleaner output layout
- Optional emphasis (headers, spacing)

---

# 🔜 V3 — Retrieval & Accuracy

## 🎯 Goal
Improve correctness for multi-project questions

### Improvements

- Better handling of:
- “list all projects”
- “how many projects”
- More consistent cross-document coverage
- Reduce missed relevant projects

---

## Potential approaches

- Better prompting for aggregation
- Metadata-aware retrieval (later)

---

# 🔮 V4 — Metadata & Structure

## 🎯 Goal
Make the system more “queryable” like a database

### Add metadata to documents:

```python
{
"project": "skim-job-ai",
"type": "cli tool",
"focus": "decision-making",
"tech": ["Python", "Ollama"]
}
````

***

### Enable queries like:

* “Which projects use Ollama?”
* “Which tools are browser-based?”
* “Which projects focus on learning vs decision-making?”

***

# 🔮 V5 — Insight Layer (High Value)

## 🎯 Goal

Go beyond answers → generate meaningful insights

### Examples

* “What themes exist across my projects?”
* “How has my thinking evolved?”
* “What should I build next?”

***

### Improve:

* pattern extraction
* developer profiling
* suggestion generation

***

# 🔮 V6 — Persistence & Performance

## 🎯 Goal

Make the tool faster and more practical

### Improvements

* Persist index (avoid rebuilding on each query)
* Cache embeddings
* Faster response times

***

# 🔮 V7 — Expanded Data Sources

## 🎯 Goal

Move beyond README-only knowledge

### Add:

* `FEEDBACK.md` (learning signals)
* notes / ideas
* experimental logs
* project context files

***

### Result

👉 A richer, more personal knowledge base

***

# 🔮 V8 — CLI as Daily Tool

## 🎯 Goal

Make this something you actually use regularly

### Possible commands:

```
projects-ai ask "..."
projects-ai list
projects-ai count
projects-ai suggest
```

***

### Example

```
projects-ai suggest "What should I build next?"
```

***

# 🔮 V9 — Reflection & Self-Understanding

## 🎯 Goal

Use the system as a reflection tool

### Example questions:

* “What motivates my projects?”
* “What problems do I keep solving?”
* “Where do I focus my effort?”

***

👉 This is where the project becomes:

> not a tool → but a **mirror**

***

# ⚠️ Non-Goals (Important)

This project is intentionally NOT:

* a full knowledge base system
* a production-grade search engine
* a complex AI platform

***

👉 Keep it:

* simple
* personal
* useful

***

# 🔁 Feedback Loop

This project evolves through:

```
Ask → Observe → Log (FEEDBACK.md) → Improve → Repeat
```

***

👉 The `FEEDBACK.md` file is the most important driver of progress.

***

# ✅ Summary

projects-ai evolves like this:

1. Search → answers
2. Answers → structure
3. Structure → insights
4. Insights → reflection

👉 Final goal:

> “Understand your own work better than you currently do”

```

---

# 🧠 Why this roadmap works for you

This is very aligned with your style:

- ✅ minimal first  
- ✅ feedback-driven evolution  
- ✅ practical improvements (not theory)  
- ✅ slowly increases capability  

---

# 🔥 One key thing to notice

The roadmap is **not about adding features**  
It’s about increasing:

> **insight quality**

---

# 🚀 Suggested next step (after this)

Now that you have a roadmap:

👉 Go back to the tool and use it for 10–15 real queries

Then:

- add 2–3 FEEDBACK entries  
- observe where it breaks / feels weak  

---

👉 THAT will tell you which roadmap step matters most next

---

# 👀 If you want next step with me

We can now do:

✅ “dashboard-style output” (high signal / low noise)  
✅ or “make suggestions (what should I build next?) really good”

---

Just tell me 👍
```
