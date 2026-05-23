# Project: skim-job-ai

## Description

A CLI tool that helps you instantly decide whether a job posting is worth your attention.

Instead of reading full job ads, the tool provides a compressed summary, key requirements, and a quick verdict so you can decide in seconds:
👉 “Is this worth my time?”

---

## Purpose

Job postings are often:

- too long
- full of buzzwords
- cognitively exhausting

This tool acts as a **decision accelerator**, reducing friction and helping you act faster.

---

## Key Idea

This is NOT a traditional job evaluation tool.

It is designed to:

- remove noise
- highlight signal
- help you decide quickly

👉 Not: “understand everything”  
👉 But: “decide fast”

---

## Input / Output

### Input

- Job posting URL

### Output

- 📄 Job summary (ultra condensed)
- ✅ Must-have skills
- 👍 Nice-to-have skills
- ⚙️ What you’ll actually do
- 🚦 Verdict (🟢 Yes / 🟡 Maybe / 🔴 No)

---

## Example

Command:

```

python main.py <https://example.com/job>

```

Output:

```

Job Summary:
Backend/data role in energy sector

Must-have:

* Python / C# / Java
* ETL / pipelines
* Databricks / Synapse

Nice-to-have:

* Kubernetes
* Energy domain knowledge

What you'll do:

* Build data applications
* Maintain pipelines
* Create reporting tools

=== VERDICT ===
🟢 Yes

```

---

## Verdict System

The verdict is computed locally based on your preferences:

- 🟢 Yes → strong match
- 🟡 Maybe → partial match
- 🔴 No → low relevance

This is intentionally strict to reduce noise.

---

## Architecture

Job URL  
↓  
Trafilatura (content extraction)  
↓  
LLM (compression via Ollama)  
↓  
Structured output  
↓  
Python logic (verdict)

---

## Tech Stack

- Python
- Ollama (LLM)
- Trafilatura
- CLI-based interface

---

## Scope

This project is intentionally limited.

It does NOT:

- analyze your CV
- rank jobs
- attempt full job matching

It only answers:
👉 “Should I even look at this?”

---

## Usage

```

python main.py \<job\_url>

```

Example:

```

python main.py <https://company.com/job-posting>

```

---

## Future Ideas

- Clipboard support (paste URL → result)
- Browser extension
- Smarter verdict scoring
- Output formatting improvements
- Job filtering workflows

---

## Philosophy

Reduce friction → increase action

- Less reading
- Less overthinking
- More progress
