import os
from chromadb import PersistentClient
from chromadb.config import Settings
from chromadb.utils import embedding_functions

client = PersistentClient(path=os.getenv("CHROMA_DB_DIR", "./vector_store"))

collection = client.get_or_create_collection(
    name="endian_docs",
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    )
)    

def clear_collection():
    collection.clear()

def add_documents(docs, metadatas):
    collection.add(documents=docs, metadatas=metadatas, ids=[str(i) for i in range(len(docs))])

def query_docs(query, n_results=5):
    return collection.query(query_texts=[query], n_results=n_results)
