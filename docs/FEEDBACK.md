# FEEDBACK.md

## 🎯 Purpose

This file documents observations about the RAG system behavior in `projects-ai`.

The goal is to:

- understand when the system performs well ✅
- identify failure patterns ❌
- guide improvements (prompting, structure, retrieval)

This is NOT about perfect evaluation —  
this is about **learning through real usage**.

---

## 🧠 Evaluation mindset

RAG systems are:

- probabilistic
- context-dependent
- sensitive to structure and prompts

So instead of expecting correctness, we focus on:

- usefulness
- clarity
- completeness
- consistency

---

# 📋 Test Entry Template (copy this)

## Test case: <short title>

**Query**

```
<your question>
```

**Result**

```
<paste model output>
```

**Expected behavior**

- What SHOULD the system have done?

**Observed issues**

- What went wrong?
- Be concrete (missing info, vague answer, wrong reasoning)

**Quality assessment**

- Correctness: ✅ / ⚠️ / ❌
- Completeness: ✅ / ⚠️ / ❌
- Usefulness: ✅ / ⚠️ / ❌

**Type of question**

- [ ] Single-project (easy)
- [ ] Multi-project (cross-doc reasoning)
- [ ] Aggregation (list/count)
- [ ] Reflection (patterns / suggestions)

**Hypothesis (why it failed or succeeded)**

- Retrieval issue?
- Prompt too weak?
- Document structure unclear?

**Next step**

- What should be improved?
  - prompt
  - document structure
  - retrieval
  - ignore (acceptable limitation)

---

# 🧪 Entries

## Test case: Identify tech usage across projects

**Query**

```
Which projects use Ollama?
```

**Result**

```
The system mentioned only one project or gave a vague answer.
```

**Expected behavior**

- Should list:
  - skim-job-ai
  - fastapi-ollama-template

**Observed issues**

- Did not aggregate across documents
- Missed structured "Tech Stack" sections

**Quality assessment**

- Correctness: ⚠️
- Completeness: ❌
- Usefulness: ⚠️

**Type of question**

- [ ] Single-project
- [x] Multi-project
- [x] Aggregation
- [ ] Reflection

**Hypothesis**

- Retrieval may only return top chunks
- Model not explicitly instructed to extract & compare

**Next step**

- Improve prompt to:
  - explicitly extract tech usage
  - encourage listing items across documents

---

## Test case: Bulleted output for longer answers

**Query**

```
"What is skim-job-ai about?"
```

**Result**

```
"A CLI tool that helps you instantly decide whether a job posting is worth your attention by providing a compressed summary, key requirements, and a quick verdict so you can decide in seconds."
```

**Expected behavior**

Since the answer was fairly long - though very good - it could have given an answer like this:

"A CLI tool that helps you instantly decide whether a job posting is worth your attention by providing

- a compressed summary
- key requirements
- a quick verdict so you can decide in seconds."

**Observed issues**

- Nothing really went wrong
- Could've provided a better overview of project using bullet points

**Quality assessment**

- Correctness: ✅
- Completeness: ✅
- Usefulness: ⚠️

**Type of question**

- [x] Single-project (easy)
- [ ] Multi-project (cross-doc reasoning)
- [ ] Aggregation (list/count)
- [ ] Reflection (patterns / suggestions)

**Hypothesis (why it failed or succeeded)**

- Prompt might have been too weak or unstructured to provide the answer in format I would really have like (i.e. given me a better overview)

**Next step**

- What should be improved?
  - prompt

---

## Test case: Good answer about cross-project question

**Query**

```
"Which projects focus on reducing friction?"
```

**Result**

```
Based on the provided context information, I can identify two projects that aim to reduce friction:

• **should-i-read-this**: This project aims to reduce decision-making friction by providing an AI-generated summary of Real Python articles, allowing you to quickly decide whether to read it.
• **skim-job-ai**: This CLI tool reduces friction by compressing job postings into ultra-condensed summaries, key requirements, and a quick verdict, enabling you to make decisions in seconds.

These projects aim to streamline processes, eliminate unnecessary reading, and save time for users.
```

**Expected behavior**

It actually provided a really, really good answer that correctly identified the (only) two project that reduces friction - so it should not have done anything else (probably)

**Observed issues**

No issue. Even based on a (very) small sample of md files it provided a very good answer

**Quality assessment**

- Correctness: ✅
- Completeness: ✅
- Usefulness: ✅

**Type of question**

- [ ] Single-project (easy)
- [x] Multi-project (cross-doc reasoning)
- [ ] Aggregation (list/count)
- [x] Reflection (patterns / suggestions)

**Hypothesis (why it failed or succeeded)**

It didn't fail on a small data sample (whether that would be the case on a larger sample - I don't know)

**Next step**

- What should be improved?
  - Nothing actually (as of right now)
