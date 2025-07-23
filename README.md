# 🧠 Endian RAG Assistant

This project is a lightweight **Retrieval-Augmented Generation (RAG)** prototype designed to support Sales Engineers and Key Account Managers at **Endian** by enabling natural language search over internal documents like sales decks, whitepapers, and proposals.

Built using:
- OpenAI GPT-4 / GPT-3.5 API
- Instructor-XL for embedding
- Chroma as local vector store
- Streamlit for an easy-to-use frontend

---

## 🚀 What It Does

- Reads and processes internal PDFs (`app/data`)
- Converts them into vector embeddings using `InstructorEmbedding`
- Stores them in a **local Chroma vector store**
- Allows you to **ask natural language questions** through a chat interface
- Answers are generated using OpenAI models, grounded in your documents

---

## 🧱 Project Structure

```text
RAG-ENDIAN/
├── app/
│   ├── streamlit_app.py        # Streamlit UI
│   ├── prompts/system_prompt.txt
│   └── data/                   # Input PDF documents
│
└── loaders/
    └── pdf_loader.py           # PDF parsing logic
│
├── rag_engine/                 # Core logic for RAG pipeline
│   ├── __init__.py
│   ├── embedder.py             # Embedding using Instructor-XL
│   ├── retriever.py            # Chroma vector search
│   └── rag_chain.py            # Prompt assembly + OpenAI call
│
├── vector_store/               # Persisted Chroma DB
│   └── chroma.sqlite3
│
├── run_pipeline.py             # CLI script to ingest new PDFs
├── .env                        # OpenAI API key (not committed)
├── requirements.txt            # Dependencies
└── README.md                   # You're reading it!
```

## 🧪 Setup Guide
1. Create a Virtual Environment
```
python -m venv rag-env
source rag-env/bin/activate  # or .\rag-env\Scripts\activate on Windows
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Add Your OpenAI API Key
Create a .env file in the root directory:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

## 📥 Add and Ingest Documents
Place your PDFs inside app/data/

Run the following command to ingest them:

```
python run_pipeline.py
```

This will:

Load and chunk PDFs

Embed chunks using InstructorEmbedding

Store vectors in vector_store/ using Chroma

## 💬 Start the Chatbot (Streamlit UI)
```
streamlit run app/streamlit_app.py
```

Then:

Go to http://localhost:8501

Ask questions like:

"What are the main features of the Secure Digital Platform?"

"Summarize our renewable energy use case."

See markdown-formatted answers sourced from the PDFs you uploaded

## 🧠 How It Works (Simplified)
```
graph TD
    A[PDF Files] --> B[Chunking & Embedding]
    B --> C[Chroma Vector Store]
    D[User Question] --> E[Embedding + Retrieval]
    C --> F[Relevant Chunks]
    F --> G[Prompt + Context]
    G --> H[OpenAI GPT-4/GPT-3.5]
    H --> I[Answer Displayed in UI]
```

## 🛠 Key Modules
File	Responsibility
pdf_loader.py	PDF parsing via PyMuPDF
embedder.py	Embedding with InstructorEmbedding
retriever.py	Vector search using Chroma
rag_chain.py	Prompt assembly + OpenAI completion
streamlit_app.py	Chat UI to interact with the system
run_pipeline.py	Command-line document ingestion

## ✅ Next Steps
Add support for DOCX, HTML or Confluence exports

Enable multi-user support + authentication

Integrate FAQs or Zendesk tickets for customer service

## 👤 Maintainer
Filippo Collini
Sales Engineer & Key Account Manager at Endian
GitHub

## 🛡 Security Note
This prototype uses local storage and only sends data to OpenAI's API for completions. Do not include sensitive or confidential client data unless secure APIs and environments are enforced.
