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

* What SHOULD the system have done?

**Observed issues**

* What went wrong?
* Be concrete (missing info, vague answer, wrong reasoning)

**Quality assessment**

* Correctness: ✅ / ⚠️ / ❌
* Completeness: ✅ / ⚠️ / ❌
* Usefulness: ✅ / ⚠️ / ❌

**Type of question**

* [ ] Single-project (easy)
* [ ] Multi-project (cross-doc reasoning)
* [ ] Aggregation (list/count)
* [ ] Reflection (patterns / suggestions)

**Hypothesis (why it failed or succeeded)**

* Retrieval issue?
* Prompt too weak?
* Document structure unclear?

**Next step**

* What should be improved?
  * prompt
  * document structure
  * retrieval
  * ignore (acceptable limitation)

***

# 🧪 Example Entry

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

* Should list:
  * skim-job-ai
  * fastapi-ollama-template

**Observed issues**

* Did not aggregate across documents
* Missed structured "Tech Stack" sections

**Quality assessment**

* Correctness: ⚠️
* Completeness: ❌
* Usefulness: ⚠️

**Type of question**

* [ ] Single-project
* [x] Multi-project
* [x] Aggregation
* [ ] Reflection

**Hypothesis**

* Retrieval may only return top chunks
* Model not explicitly instructed to extract & compare

**Next step**

* Improve prompt to:
  * explicitly extract tech usage
  * encourage listing items across documents

***

