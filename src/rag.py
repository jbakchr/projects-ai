# src/rag.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# --- CONFIGURATION ---

def configure_models():
    """Configure LLM and embedding model (Ollama)"""
    Settings.llm = Ollama(
        model="llama3",
        request_timeout=120.0,
    )

    Settings.embed_model = OllamaEmbedding(
        model_name="nomic-embed-text"
    )


# --- LOAD + INDEX ---

def build_index(data_dir: str = "./data"):
    """Load documents and create index"""
    documents = SimpleDirectoryReader(data_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index


# --- QUERY ---

def query_projects(question: str):
    configure_models()
    index = build_index()

    query_engine = index.as_query_engine(
        response_mode="compact"
    )

    # ✅ Wrap the question with formatting instructions
    enhanced_question = f"""
You are analyzing a set of personal software projects.

Your goal is to produce a HIGH-VALUE, SCANNABLE answer that helps decision-making.

---

Return your answer using EXACTLY this structure:

## Answer
A short, direct answer to the question (1–2 sentences max)

## Key Points
- Max 2 bullets
- Only include points that directly influence the suggestion

## Suggestion
Propose 1–2 specific project ideas.

Each idea must be formatted like this:
- <Project name>: <what it does> → <why it's useful or interesting>

Additional constraints:
- Must NOT repeat or closely resemble existing projects
- Must introduce a clear twist, improvement, or new angle
- Must combine or extend patterns in a new way
- Must be specific and buildable as a small tool
- At least one suggestion should feel slightly surprising or non-obvious (something the developer likely hasn’t already considered)

Avoid:
- Rephrasing existing ideas
- Minor variations of current projects
- Generic "summarizer" or "filtering tool" ideas

Prefer:
- New combinations of existing patterns
- Slightly surprising but practical ideas

---

Formatting rules:
- Be concise and dense (no fluff)
- Prefer bullets over paragraphs
- Avoid repetition
- Avoid generic phrases
- Use concrete language
- ALWAYS use "-" for bullet points (never "*")

Quality rules:
- Every section must add value
- If data is weak or incomplete, say so briefly
- Do NOT hallucinate projects or details
- Prioritize usefulness over completeness
- If the question asks for ideas, prioritize originality over safety

---

Question:
{question}
"""



    response = query_engine.query(enhanced_question)

    return str(response)