import os
from loaders.pdf_loader import load_pdf
from rag_engine.embedder import add_documents
from rag_engine.embedder import clear_collection

from dotenv import load_dotenv
load_dotenv()

def main():
    import shutil
    import os

    # Delete old Chroma DB before creating new one
    vector_store_path = "vector_store"
    if os.path.exists(vector_store_path):
        shutil.rmtree(vector_store_path)

    docs_dir = "data"
    for filename in os.listdir(docs_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(docs_dir, filename)
            text = load_pdf(path)
            chunks = [text[i:i+500] for i in range(0, len(text), 500)]
            metadatas = [{"source": filename}] * len(chunks)
            add_documents(chunks, metadatas)
            print(f"Indexed: {filename}")

if __name__ == "__main__":
    main()

