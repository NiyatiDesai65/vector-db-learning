import chromadb

#Start a db
#client = chromadb.Client()
client = chromadb.PersistentClient(path="./my_database")

#creates a connection
collection = client.create_collection("my_collection")

#every row needs unique id
collection.add(
    documents=[
        "my payment is not working",
        "I cannot login to my account",
        "the app keeps crashing on my phone",
        "I was charged twice for my order",
        "forgot my password and cant reset it"
    ],
    ids=["1", "2", "3", "4", "5"]  
)

results = collection.query(query_texts=["I cant access my account"],  
    n_results=2)

print("You searched for: I cant access my account")
print("Most similar results found:")
for doc in results['documents'][0]:
    print(" →", doc)
    
searches = [
    "billing problem",
    "phone issue",
    "account problem"
]

print("\n--- Trying more searches ---")
for search in searches:
    results = collection.query(
        query_texts=[search],
        n_results=1
    )
    print(f"\nSearch: '{search}'")
    print(f"Result: {results['documents'][0][0]}")