# projects-ai – Prompt Guidelines

---

## 🧠 Purpose of this file

This file defines how prompts in `projects-ai` should be designed.

The goal is not to experiment randomly.  
The goal is:

👉 **consistently generate high-value, actionable ideas**

---

## 🎯 Core principle

The system is not meant to:

- explain
- summarize
- analyze deeply

The system is meant to:

👉 **trigger action and generate ideas**

---

## ✅ What a good output looks like

A good answer:

- is fast to read (high signal)
- is easy to scan
- contains at least one idea worth considering
- sometimes feels slightly surprising
- creates a sense of:
  👉 “I could build something now”

---

## 🧱 Current output structure

```
## Answer
(short directional statement)

## Key Points
(1–2 bullets that justify the direction)

## Suggestion
(1–2 concise project ideas)
```

---

## 🧠 Section roles (very important)

### Answer

- Acts as a **trigger**
- Should give a sense of direction
- Not meant to be perfect or deep

---

### Key Points

- Acts as **justification**
- Answers:
  👉 “Why these suggestions?”
- Must be:
  - minimal
  - relevant
  - decision-supporting (not descriptive)

---

### Suggestion (most important)

- This is the **core value of the system**
- Everything else supports this section

---

## 🔥 Suggestion design rules

Each suggestion must:

- be **1 line only**
- follow format:

```
- <name>: <what it does> → <why it matters>
```

---

## ✅ Required constraints

Each suggestion must:

- NOT repeat existing projects
- NOT be a minor variation
- combine patterns in a new way
- be buildable as a small tool
- match style:
  - CLI-first or minimal UI
  - friction-reducing
  - practical / personal use

---

## 🔥 Critical constraint

At least ONE suggestion must:

👉 feel slightly surprising or non-obvious

This is what creates:

- curiosity
- new directions
- real value

---

## ❌ Avoid

Avoid suggestions that are:

- generic (“build a platform”, “build a system”)
- obvious (“another summarizer”)
- too broad
- enterprise-style ideas
- something that already exists in `/data`

---

## ✅ Prefer

Prefer ideas that are:

- specific
- slightly niche
- personally useful
- quick to build (small scope)
- combining existing patterns in new ways

---

## 🧠 Key learnings from iteration

### 1. Structure > raw model output

Without structure → bad answers  
With structure → usable outputs

---

### 2. Shorter is better

- Verbosity reduces usefulness
- CLI = scan speed matters

---

### 3. Insight sections were removed

Reason:

- low value
- often generic
- not actionable

---

### 4. Suggestions drive everything

- Most valuable part of output
- Main focus for improvement

---

### 5. Constraints improve quality

Explicit constraints like:

- “no repetition”
- “must be surprising”

→ significantly improve outputs

---

## ⚖️ Tradeoffs (important to understand)

| Tradeoff                   | Decision          |
| -------------------------- | ----------------- |
| Depth vs speed             | prefer speed      |
| Explanation vs action      | prefer action     |
| Completeness vs usefulness | prefer usefulness |

---

## 🧭 When modifying the prompt

Follow this process:

```
Change ONE thing → test → observe → log → repeat
```

Never:

- change multiple sections at once
- redesign everything
- overengineer

---

## ✅ Evaluation checklist

After each change, ask:

- Did I read the full output?
- Did I get at least one interesting idea?
- Did it make me want to build something?

If YES → keep  
If NO → adjust

---

## 🔮 Possible future additions

(Do not implement yet)

- “First step” (micro-action)
- slightly more opinionated suggestions
- better idea variation

---

## 🚫 Non-goals

- Perfect accuracy
- Complete coverage
- Deep analysis
- Complex reasoning pipelines

---

## 🧠 Final principle

If a change makes the output:

- more complex ❌
- longer ❌
- harder to scan ❌

→ it is probably wrong

If it makes the output:

- faster ✅
- sharper ✅
- more actionable ✅

→ it is probably right

---
