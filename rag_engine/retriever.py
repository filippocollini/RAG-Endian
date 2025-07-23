from rag_engine.embedder import query_docs

def retrieve_relevant_chunks(query):
    results = query_docs(query)
    return results['documents'][0]
