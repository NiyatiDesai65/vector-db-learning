# Smart Document Search

An AI-powered document search system that lets you ask questions 
in plain English and get answers from any text document.

Built using Python, ChromaDB and Claude AI.

## What this does
- Reads any text document
- Splits it into chunks using sentence based chunking with overlap
- Stores chunks in a vector database as embeddings
- Lets you ask questions in plain English
- Claude answers using only the relevant parts of your document
- Says "I don't have that information" if answer is not in document

## Tech used
- Python
- ChromaDB (vector database)
- Anthropic Claude API
- RAG (Retrieval Augmented Generation)
- Sentence based chunking with overlap

## How it works
1. Document is read and split into sentences
2. Every 3 sentences become one chunk with 1 sentence overlap
3. Chunks are stored in ChromaDB as embeddings
4. User asks a question
5. Question is searched against vector database
6. Top 2 matching chunks are sent to Claude as context
7. Claude answers using only that context

## How to run
pip install chromadb anthropic python-dotenv

Create a .env file:
ANTHROPIC_API_KEY=your-key-here

Run:
python search.py

## Example
Question: What is machine learning?
Answer: Machine learning is a subset of AI that learns from 
        data without being programmed.

Question: What is the capital of France?
Answer: I don't have that information.