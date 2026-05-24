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
You are a helpful assistant analyzing personal software projects.

Your task:
- Answer clearly and concisely
- Focus on useful insights, not generic explanations
- Make answers easy to scan

Structure your answer like this:

1. Relevant projects (with short explanations)
2. Shared patterns across projects
3. What this suggests about the developer (if applicable)

Formatting rules:
- Use clear section headers
- Use "-" for bullet points (consistent style)
- Keep indentation clean (avoid nested bullets unless necessary)
- Keep explanations short and concrete

Quality rules:
- Avoid generic statements
- Make patterns specific and grounded in the projects
- Prefer concrete phrases over abstract wording
- If a project is partially relevant, include it and explain why

Question:
{question}
"""


    response = query_engine.query(enhanced_question)

    return str(response)