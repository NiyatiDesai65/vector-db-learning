# Vector Database & RAG Learning Project

A hands-on project to learn vector databases and semantic search using Python, ChromaDB and Claude AI.

## What this does
- Stores text and searches it by meaning, not exact keywords
- Splits large documents into chunks for better search
- Uses RAG (Retrieval Augmented Generation) to answer questions from documents using Claude AI

## Tech used
- Python
- ChromaDB
- Anthropic Claude API
- RAG (Retrieval Augmented Generation)

## Projects
- `basics.py` — basic vector database with semantic search
- `chunking.py` — splitting documents into chunks
- `rag_document_search/` — ask questions to any document using Claude AI

## How to run
pip install chromadb anthropic python-dotenv

Create a .env file with your Anthropic API key:
ANTHROPIC_API_KEY=your-key-here

Then run any file:
python basics.py
python chunking.py
python rag_document_search/ask_your_documents.py