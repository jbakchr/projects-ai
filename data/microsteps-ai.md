# Project: microsteps-ai

## Description

A CLI tool that generates small, actionable micro-steps to help you start tasks with less resistance.  
Instead of planning or optimizing, the tool focuses on one thing:

👉 “What is the smallest step I can take right now?”

---

## Purpose

Starting tasks is often harder than doing them.

Common issues:

- overthinking
- too much scope
- unclear first action  
  This tool acts as a **friction reducer**, helping initiate action through tiny, concrete steps.

---

## Key Idea

This is NOT a productivity planner.

It is designed to:

- lower activation energy
- make starting feel trivial
- create momentum through small actions

👉 Not: “plan everything”  
👉 But: “just start”

---

## Input / Output

## Input

- A task description  
  (e.g. "clean kitchen", "write README")

## Output

- 3 micro-steps:
  - small
  - sequential
  - easy to start

---

## Example

Command:

```bash
python test_cli.py
```

Input:

```
clean kitchen
```

Output:

```
Step 1: Pick up one dirty dish
Step 2: Put it in the sink
Step 3: Wipe down the counter beside it
```

---

## Core Behavior

- Uses a local LLM (Ollama)
- Generates a short sequence of steps
- Prioritizes:
  - simplicity
  - continuity
  - actionability

---

## Important Learnings

- ✅ Step 1 is the most important  
  → it must be extremely easy to start

- ✅ Steps work best when:
  - they share the same context
  - they build on each other
  - they form a small flow

- ✅ Steps 2–3 are optional  
  → they guide continuation, not obligation

- ✅ Smaller = better  
  → “too easy” is actually ideal

---

## Architecture

Task input  
↓  
LLM (via Ollama)  
↓  
Micro-step generation  
↓  
Structured output

---

## Tech Stack

- Python
- Ollama (local LLM)
- CLI interface

---

## Scope

This project is intentionally limited.

It does NOT:

- manage tasks
- store history
- optimize workflows
- build full plans

It only answers:

👉 “What is the easiest possible first step?”

---

## Usage

```bash
python test_cli.py
```

Example:

```
Input: write README
Output: 3 small steps to begin writing
```

---

## Feedback Loop

All real usage is tracked in:

👉 FEEDBACK.md

Each entry captures:

- Input
- Output
- Felt usefulness
- Whether action happened

---

## Philosophy

Reduce friction → enable action

- No overthinking
- No complexity
- Just start

---

## Why this project matters

This project explores a key idea:

👉 Action often comes from **starting**, not planning

Even a single small step can:

- reduce resistance
- create momentum
- trigger delayed action later

---

## Future Ideas

- Better input guidance (more specific prompts)
- Different modes (start vs continue)
- Lightweight UI
- Pattern learning from feedback

---

## Current State

- ✅ Core behavior works
- ✅ CLI is sufficient
- ✅ Output is action-oriented
- ✅ Active feedback loop

The project is currently in a:

👉 usage + learning phase

---

## License

MIT
