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
- 3–5 concise bullet points
- Focus on concrete facts

## Cross-Project Patterns (if applicable)
- Only include if relevant
- Focus on repeated behaviors, tools, or design choices

## Suggestion
What the developer should consider doing next
→ Make it actionable and grounded in the analysis

---

Formatting rules:
- Be concise and dense (no fluff)
- Prefer bullets over paragraphs
- Avoid repetition
- Avoid generic phrases
- Use concrete language

Quality rules:
- Every section must add value
- If data is weak or incomplete, say so briefly
- Do NOT hallucinate projects or details
- Prioritize usefulness over completeness

---

Question:
{question}
"""


    response = query_engine.query(enhanced_question)

    return str(response)