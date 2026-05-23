# src/rag.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# --- CONFIGURATION ---

def configure_models():
    """Configure LLM and embedding model (Ollama)"""
    Settings.llm = Ollama(
        model="llama3.1:8b",
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
    """Run a query against indexed project data"""
    configure_models()
    index = build_index()

    query_engine = index.as_query_engine()
    response = query_engine.query(question)

    return str(response)