# Project: email-ai-assistant

## Description

A Chrome Extension + backend system that generates context-aware email replies directly inside Gmail using AI.

👉 “Reply to emails faster — without writing from scratch”

---

## Purpose

Writing emails is often:

- repetitive
- time-consuming
- mentally draining

This tool acts as a **drafting assistant**, helping you:

- generate replies instantly
- reduce effort
- stay accurate

---

## Key Idea

This is NOT an auto-reply system.

It is designed to:

- generate a useful draft
- respect real-world constraints
- let you stay in control

👉 Not: “send emails automatically”  
👉 But: “help you respond faster”

---

## Input / Output

## Input

- Email content (from Gmail)
- Optional context (about you / situation)

## Output

- A suggested reply inserted directly into Gmail compose

---

## Example

Workflow:

```

1. Open email in Gmail
2. Click "✨ AI Reply"
3. Draft reply appears in compose box
4. Edit (if needed) and send

```

---

## Core Behavior

- Extracts email content from Gmail
- Sends to backend
- Generates reply using LLM
- Inserts directly into the UI

---

## Key Feature

## Context-aware replies

The system uses structured prompting:

```

SYSTEM → rules (no hallucinations)
CONTEXT → user-specific facts
EMAIL → input message
→ OUTPUT → reply

```

---

## Why this matters

Without context:

- ❌ AI guesses → incorrect replies

With context:

- ✅ Replies reflect real-world constraints
- ✅ Less risk of wrong information

---

## Architecture

Email (Gmail UI)  
↓  
Chrome Extension (extract + trigger)  
↓  
FastAPI backend  
↓  
LLM (Ollama)  
↓  
Generated reply  
↓  
Inserted into compose box

---

## Tech Stack

- Python
- FastAPI
- Ollama (LLM)
- Chrome Extension (JavaScript)

---

## Scope

This project is intentionally limited.

It does NOT:

- send emails automatically
- manage inboxes
- replace human judgment

It only helps with:

👉 generating a useful reply draft

---

## Usage

1. Install Chrome extension
2. Start backend:

```bash
uvicorn main:app --reload
```

3. Open Gmail and use:

```
✨ AI Reply
```

---

## Current Strengths

- ✅ Real workflow integration (Gmail)
- ✅ Context-aware replies
- ✅ Reduces writing effort significantly
- ✅ Works for:
  - practical emails
  - invitations
  - service-related questions

---

## Limitations

- Replies can be:
  - slightly too long
  - overly formal
- Basic email parsing
- Static context (hardcoded)
- No UI for regeneration/editing
- Limited thread awareness

---

## Feedback Loop

The system improves via:

👉 FEEDBACK.md

Tracking:

- Email input
- Generated reply
- Needed edits
- Real usefulness

---

## Philosophy

Reduce effort → keep control

- Assist, don’t automate
- Correctness > cleverness
- Context > generic AI

---

## Why this project matters

This project explores:

👉 AI integrated directly into real workflows

It shows that:

- usefulness comes from context
- small automations can save real time
- AI works best as a drafting assistant

---

## Future Ideas

- “Regenerate reply” button
- Inline suggestion UI
- Dynamic context (based on email)
- Tone control (short / friendly / formal)
- Better handling of threads

---

## Current State

- ✅ Fully usable in real workflow
- ✅ Integrated into Gmail
- ✅ Produces useful draft replies
- ✅ Active usage + iteration

---

## License

MIT
