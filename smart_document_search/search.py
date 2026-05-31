import chromadb
import anthropic
import os
from dotenv import load_dotenv
import re

load_dotenv()

#steps:
# 1. Read document from file
# 2. Chunk the document
# 3. Store in vector db
# 4. search and answer
# 5. Main Program

# Read document from file

def read_document(filepath):
    with open(filepath,'r') as f:
        return f.read()

#chunk the document 
# Splitting document with each sentence and 3 sentence will make one chunk    
def chunk_document(text,sentences_per_chunk = 3):
    sentences = re.split(r'(?<=[.!?])\s+',text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    
    chunks = []
    i=0
    
    while i<len(sentences):
        chunk_sentences = sentences[i:i+sentences_per_chunk]
        chunk = ' '.join(chunk_sentences)
        chunks.append(chunk)
        i += sentences_per_chunk - 1
        
    return chunks
    
#store chunks in vector db
def store_chunks(chunks,collection_name="documents"):
    chromadb_client = chromadb.PersistentClient(path="./document.db")
    
    try:
        chromadb_client.delete_collection(collection_name)
    except:
        pass
    
    collection = chromadb_client.create_collection(collection_name)
    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    return collection

def ask_question(question,collection):
    results = collection.query(
        query_texts = [question],
        n_results =2
    )
    
    context = "\n".join(results['documents'][0])
    
    anthropic_client = anthropic.Anthropic()
    response = anthropic_client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Answer the question using only the context below.
                If the answer is not in the context, say 'I don't have that information.'

                Context:
                {context}

                Question: {question}
                """
            }
        ]
    )
    
    return response.content[0].text
    

def main():
    print("----------- Document Search--------------")
    
    #read and process document
    filepath = "sample.txt"
    print(f"Reading document : {filepath}")
    text = read_document(filepath)
    
    chunks = chunk_document(text)
    
    collection = store_chunks(chunks)
    
    print(f"Document loaded. {len(chunks)} chunks created.")
    print("\nYou can now ask questions. Type 'exit' to quit.\n")
    
    while True:
        question = input("Your Question : ").strip()
        
        if(question.lower()=="exit"):
            print("Nice talking to you - GoodBye!")
            break
        
        if not question:
            continue
        
        print("\nSearching...\n")
        answer = ask_question(question, collection)
        print(f"Answer: {answer}\n")
        print("-" * 40 + "\n")  
        
if __name__ == "__main__":
        main()