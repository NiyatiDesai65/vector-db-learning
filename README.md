# AI Data Engineering Portfolio

A collection of hands-on projects built to learn and demonstrate
AI data engineering skills using Python, ChromaDB and Claude AI.

## Projects

### 1. Vector Database Basics
Learn how vector databases work and how to search text by meaning.
- Semantic search using ChromaDB
- Document chunking with sentence overlap
- Files: `basics.py`, `chunking.py`

### 2. Smart Document Search
An interactive Q&A system that answers questions from any document.
- RAG (Retrieval Augmented Generation) system
- Sentence based chunking with overlap
- Ask questions in plain English, get answers from your document
- Folder: `smart_document_search/`

### 3. Customer Review AI Pipeline
An automated pipeline that analyses customer reviews using Claude AI.
- Reads raw reviews from CSV
- Extracts sentiment, category and summary using Claude AI
- Generates business report with actionable insights
- Folder: `customer_review_ai_pipeline/`

## Tech stack
- Python
- ChromaDB (vector database)
- Anthropic Claude API
- RAG (Retrieval Augmented Generation)
- Semantic search and embeddings

## How to run any project
pip install chromadb anthropic python-dotenv

Create a .env file in the project folder:
ANTHROPIC_API_KEY=your-key-here

Then run any project:
python basics.py
python smart_document_search/search.py
python customer_review_ai_pipeline/ai_pipeline.py

## What I learned
- How embeddings convert text to numbers
- How vector databases store and search by meaning
- How to chunk documents for better search accuracy
- How to build RAG systems that answer questions from documents
- How to build AI pipelines that process and analyse data at scale