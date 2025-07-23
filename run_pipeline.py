
import os
from loaders.pdf_loader import load_pdf
from rag_engine.embedder import add_documents

from dotenv import load_dotenv
load_dotenv()

def main():
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

