# Project: should-i-read-this

## Description

A low-friction tool that helps you decide whether a Real Python article is worth your time.

Instead of manually skimming long articles, it provides an AI-generated summary so you can quickly decide:
👉 read now, bookmark, or skip.

---

## Purpose

When learning, the real bottleneck is not lack of content — it is deciding:

👉 “Is this article worth spending time on?”

This tool reduces friction by acting as a **learning triage system**.

---

## Key Idea

This is not a summarization tool for deep understanding.

It is designed to:

- reduce decision friction
- provide fast, structured insight
- help you act quickly

👉 Not: “fully understand the article”  
👉 But: “decide whether to read it”

---

## Input / Output

### Input

- Real Python article (via browser extension)

### Output

- Structured AI-generated summary
- Recommendation for whether to read

---

## How it Works

1. Open a Real Python article
2. Click a floating button (FAB)
3. Article content is sent to backend
4. LLM generates structured summary
5. Summary is shown in modal

---

## Summary Format

Summaries are optimized for decision-making:

```

🧠 What you'll learn
📚 Key concepts
💻 Code insights
⚡ When is this useful?
✅ Worth reading if:

```

---

## Architecture

Browser (Chrome extension)  
↓  
Extract article content  
↓  
FastAPI backend  
↓  
LLM (Ollama cloud)  
↓  
Structured summary  
↓  
Modal UI display

---

## UX Design Principles

- Low friction → one click interaction
- Fast decision-making → no deep reading required
- Scannable → structured sections
- Expandable → deeper exploration if needed

---

## Modal UX

The summary is presented in a modal with:

- Scrollable content
- Clear section structure
- Code block rendering
- Optional collapsible sections
- Quick decision signal at the top

---

## Example Flow

1. Open article
2. Click button
3. Wait a few seconds
4. Read summary
5. Decide:
   - ✅ Read now
   - 🔖 Bookmark
   - ❌ Skip

---

## Tech Stack

- Frontend: Chrome Extension
- Backend: FastAPI
- LLM: Ollama Cloud (`gpt-oss:120b-cloud` or similar)
- Extraction: HTML → cleaned text

---

## Scope

This project is intentionally limited.

It does:

- summarize articles
- support decision-making

It does NOT:

- act as a knowledge base
- store long-term notes
- replace deep reading

It only answers:
👉 “Should I read this?”

---

## Usage

1. Install Chrome extension
2. Open article on realpython.com
3. Click floating button
4. View summary

---

## Future Ideas

- Save summaries
- Bookmark integration
- Track reading decisions
- Personal preference tuning

---

## Philosophy

Reduce friction → increase learning momentum

- Less time deciding
- Less overthinking
- More action

---

## Project Structure

```

backend/     # FastAPI backend
extension/   # Chrome extension
README.md

```

---

## Development Approach

Start simple:

1. Backend summarization endpoint
2. Extension button
3. Modal UI

Focus on:
👉 getting value fast, then iterating

---

## Requirements

- Python 3.10+
- Browser (Chrome)
- Ollama Cloud access

---

## Notes

- Designed for fast experimentation
- UX-first development
- Extend only when needed

---

## License

MIT
