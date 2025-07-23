import os
from chromadb import PersistentClient
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# Setup and ensure directory is writable
VECTOR_STORE_PATH = os.path.abspath(os.getenv("CHROMA_DB_DIR", "./vector_store"))
os.makedirs(VECTOR_STORE_PATH, exist_ok=True)
if not os.access(VECTOR_STORE_PATH, os.W_OK):
    raise PermissionError(f"❌ Cannot write to vector store directory: {VECTOR_STORE_PATH}")

client = PersistentClient(path=VECTOR_STORE_PATH)

collection = client.get_or_create_collection(
    name="endian_docs",
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    )
)

def clear_collection():
    # Get all documents to extract their IDs
    existing = collection.get()
    ids_to_delete = existing["ids"]
    
    if ids_to_delete:
        collection.delete(ids=ids_to_delete)


def add_documents(docs, metadatas):
    collection.add(
        documents=docs,
        metadatas=metadatas,
        ids=[str(i) for i in range(len(docs))]
    )

def query_docs(query, n_results=5):
    return collection.query(query_texts=[query], n_results=n_results)
