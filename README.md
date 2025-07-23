# RAG-Endian

A Retrieval-Augmented Generation (RAG) system implementation with advanced document processing and semantic search capabilities.

## 📖 Project Description

RAG-Endian is a RAG (Retrieval-Augmented Generation) system that combines information retrieval with generative AI models to provide accurate, contextually-aware responses. The system processes documents, creates semantic embeddings, and enables intelligent querying of your knowledge base.

### Key Features

- **Advanced Document Processing**: Support for multiple document formats (PDF, TXT, DOCX, etc.)
- **Semantic Search**: Vector-based similarity search using state-of-the-art embedding models
- **Flexible Architecture**: Modular design supporting various LLM backends
- **Scalable Storage**: Efficient vector database integration
- **Real-time Querying**: Fast retrieval and generation pipeline
- **Customizable Prompts**: Configurable prompt templates for different use cases

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/filippocollini/RAG-Endian.git
   cd RAG-Endian
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env file with your API keys and configuration
   ```

### Required Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# OpenAI API Key (if using OpenAI models)
OPENAI_API_KEY=your_openai_api_key_here

# Vector Database Configuration
VECTOR_DB_URL=your_vector_db_url
VECTOR_DB_API_KEY=your_vector_db_api_key

# Model Configuration
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
LLM_MODEL=gpt-3.5-turbo

# Application Settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

## 📋 Usage

### Basic Example

```python
from rag_endian import RAGSystem
from rag_endian.config import Config

# Initialize the RAG system
config = Config()
rag = RAGSystem(config)

# Add documents to the knowledge base
documents = [
    "path/to/document1.pdf",
    "path/to/document2.txt",
    "path/to/document3.docx"
]

# Process and index documents
rag.add_documents(documents)

# Query the system
query = "What are the main features of the system?"
response = rag.query(query)

print(f"Query: {query}")
print(f"Response: {response.answer}")
print(f"Sources: {response.sources}")
```

### Advanced Usage

```python
from rag_endian import RAGSystem, CustomPromptTemplate
from rag_endian.retrievers import VectorRetriever
from rag_endian.generators import OpenAIGenerator

# Custom configuration
config = Config(
    chunk_size=500,
    chunk_overlap=100,
    top_k=5
)

# Initialize with custom components
retriever = VectorRetriever(embedding_model="all-mpnet-base-v2")
generator = OpenAIGenerator(model="gpt-4")
prompt_template = CustomPromptTemplate(
    template="Based on the following context: {context}\n\nAnswer: {question}"
)

rag = RAGSystem(
    config=config,
    retriever=retriever,
    generator=generator,
    prompt_template=prompt_template
)

# Batch processing
results = rag.batch_query([
    "What is the main topic?",
    "What are the key findings?",
    "What are the recommendations?"
])
```

### Command Line Interface

```bash
# Process documents
python -m rag_endian process --input-dir ./documents --output-dir ./index

# Interactive query mode
python -m rag_endian query --interactive

# Single query
python -m rag_endian query --question "Your question here"

# Batch queries from file
python -m rag_endian batch --questions-file queries.txt --output results.json
```

## 🛠 Tech Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **LangChain**: Framework for LLM application development
- **Sentence Transformers**: Embedding models for semantic search
- **FAISS/Pinecone**: Vector database for similarity search
- **OpenAI API**: Large language model integration

### Document Processing
- **PyPDF2/pdfplumber**: PDF document processing
- **python-docx**: Microsoft Word document handling
- **beautifulsoup4**: HTML/XML parsing
- **tiktoken**: Token counting and text chunking

### Web Framework (if applicable)
- **FastAPI**: RESTful API development
- **Streamlit**: Web interface for demonstrations
- **uvicorn**: ASGI server

### Development Tools
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting
- **pre-commit**: Git hooks for code quality

## 📁 Project Structure

```
RAG-Endian/
├── rag_endian/
│   ├── __init__.py
│   ├── config.py
│   ├── rag_system.py
│   ├── document_processor.py
│   ├── retrievers/
│   │   ├── __init__.py
│   │   ├── base_retriever.py
│   │   └── vector_retriever.py
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── base_generator.py
│   │   └── openai_generator.py
│   └── utils/
│       ├── __init__.py
│       ├── text_processing.py
│       └── embeddings.py
├── tests/
│   ├── __init__.py
│   ├── test_rag_system.py
│   └── test_document_processor.py
├── examples/
│   ├── basic_usage.py
│   ├── advanced_usage.py
│   └── streamlit_demo.py
├── docs/
│   ├── api_reference.md
│   └── configuration.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py
└── README.md
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=rag_endian tests/

# Run specific test file
pytest tests/test_rag_system.py -v
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code formatting
black .

# Run linting
flake8 rag_endian/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.readthedocs.io/) for the RAG framework
- [Sentence Transformers](https://www.sbert.net/) for embedding models
- [OpenAI](https://openai.com/) for language model APIs
- [Hugging Face](https://huggingface.co/) for transformer models

## 📞 Contact

**Filippo Collini** - [@filippocollini](https://github.com/filippocollini)

Project Link: [https://github.com/filippocollini/RAG-Endian](https://github.com/filippocollini/RAG-Endian)

## 🔄 Changelog

### [Unreleased]
- Initial release
- Basic RAG functionality
- Document processing pipeline
- Vector search implementation
- OpenAI integration

---

⭐ **Star this repository if you find it helpful!**
