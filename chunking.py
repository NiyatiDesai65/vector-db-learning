import chromadb

document = """
Python is a programming language created in 1991.
It is widely used for data engineering and building pipelines.
Many companies use Python because it is simple and powerful.

ChromaDB is a vector database built for AI applications.
It stores text as embeddings and allows semantic search.
ChromaDB runs locally on your laptop with no setup needed.

Data engineering is the job of moving and transforming data.
Data engineers build pipelines that collect, clean and store data.
Companies need data engineers to make sense of their data.
"""

chunks = [chunk.strip() for chunk in document.split("\n\n") if chunk.strip()]

for i,chunk in enumerate(chunks):
    print(f"\n chunk {i+1}")
    print(chunk)
    
    
client = chromadb.PersistentClient(path="./my_database1")

try:
    client.delete_collection("documents")
except:
    pass

collection = client.create_collection("documents")

collection.add(
    documents=chunks,ids=[f"chunk_{i}" for i in range(len(chunks))]
)

searches = [
    "what is python used for",
    "how does chromadb work",
    "what does a data engineer do"
]

for search in searches:
    results = collection.query(
        query_texts=[search],
        n_results=1
    )
    
print(f"\nSearch: '{search}'")
print(f"Result: {results['documents'][0][0]}")