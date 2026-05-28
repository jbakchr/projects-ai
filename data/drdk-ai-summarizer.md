# Project: drdk-ai-summarizer

## Description
A Chrome extension that summarizes DR.dk news articles using a local AI model (Ollama).

With one click, it extracts article content, generates a concise summary, and displays it in a modal UI.

👉 The goal: **understand articles in seconds**

---

## Purpose

When consuming news, the bottleneck is often:

👉 “Do I need to read this entire article?”

This tool reduces friction by:
- extracting key information
- summarizing content instantly
- helping users understand articles quickly

---

## Key Idea

This is not a deep analysis tool.

It is designed to:
- compress long articles
- highlight key points
- enable fast understanding

👉 Not: “fully analyze the article”  
👉 But: “understand the core message quickly”

---

## Input / Output

### Input
- DR.dk news article (web page)

### Output
- 3-point AI-generated summary
- Displayed in modal UI

---

## How it Works

1. Open an article on DR.dk  
2. Click the floating action button  
3. Article content is extracted  
4. Sent to FastAPI backend  
5. LLM generates summary  
6. Summary displayed in modal  

---

## Summary Format

Summaries are structured as:

```

• Point 1
• Point 2
• Point 3

```

---

## Architecture

Chrome Extension  
↓  
Extract article content  
↓  
FastAPI backend  
↓  
Ollama (local LLM)  
↓  
Summary returned  
↓  
Modal UI display  

---

## Features

- Floating action button (FAB)
- Clean article extraction (title + paragraphs)
- AI-powered summarization (Ollama)
- Modal UI with formatted bullet points
- Runs locally (no external API required)

---

## Tech Stack

- Frontend: Chrome Extension
- Backend: FastAPI
- LLM: Ollama (local models)
- Extraction: HTML → cleaned text

---

## Scope

This project is intentionally limited.

It does:
- summarize DR.dk articles
- provide fast understanding

It does NOT:
- analyze content deeply
- support multiple news sites (yet)
- store summaries

It only answers:
👉 “What is this article about?”

---

## Usage

1. Start backend  
2. Start Ollama  
3. Load Chrome extension  
4. Open DR.dk article  
5. Click button  
6. View summary  

---

## Project Structure

```

backend/     # FastAPI backend
extension/   # Chrome extension
README.md

```

---

## Future Ideas

- Save summaries  
- Support more news sites  
- Improve extraction robustness  
- Add translation / simplification  
- Keyboard shortcuts  

---

## Philosophy

Reduce friction → increase understanding

- Less reading  
- Less time spent  
- Faster insight  

---

## Development Focus

This project explores:
- Chrome extension development  
- FastAPI backend design  
- Local LLM integration (Ollama)  
- Practical AI tools  

---

## Requirements

- Python 3.10+
- Ollama running locally
- Chrome browser

---

## Notes

- Works only on DR.dk (DOM-specific)
- Large articles may slow processing
- No caching implemented yet

---

## License

MIT
