import anthropic
import chromadb
from dotenv import load_dotenv
import os

load_dotenv() 

document = """
Employees are entitled to 12 sick days per year.
Sick days do not carry over to the next year.
Employees must inform their manager before 9am if taking a sick day.

Employees get 20 paid vacation days per year.
Vacation days must be approved by the manager 2 weeks in advance.
Unused vacation days can be carried over up to a maximum of 5 days.

Work from home is allowed 3 days per week.
Employees must be available on Slack between 10am and 4pm on work from home days.
Work from home is not allowed during the first month of joining.

Health insurance is provided to all full time employees.
Insurance covers the employee and up to 3 family members.
Dental and vision are included in the insurance plan.
"""
#Splitting into chunks
chunks = [chunk.strip() for chunk in document.split("\n\n") if chunk.strip()]

#storing in vector db
chroma_client = chromadb.PersistentClient("./my_database")

try:
    chroma_client.delete_collection("CompanyPolicy")
except:
    pass

collection = chroma_client.create_collection("CompanyPolicy")


collection.add(
    documents=chunks,
    ids=[f"chunk{i}"for i in range(len(chunks))]
)
print("\n------------------------------------------------")
print("\nDocument successfully stored in vector database.")
print("\n------------------------------------------------")


#-----RAG-----
#search vector db for relevant chunks
def ask_question(question):
    results = collection.query(
        query_texts=[question],
        n_results =2
    )
    
    relevant_chunks = results['documents'][0]
    context = "\n".join(relevant_chunks)

    anthropic_client = anthropic.Anthropic()

    response = anthropic_client.messages.create(
        model = "claude-sonnet-4-5",
        max_tokens=500,
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

print("\n-----------------------------------")
print("\n Questions ")
print("\n-----------------------------------")

questions = [
    "How many sick days do I get?",
    "Can I work from home every day?",
    "Does insurance cover my family?",
    "What is the salary?"  # this is not in the document
]

for question in questions:
    print(f"Question: {question}")
    answer = ask_question(question)
    print(f"Answer: {answer}")



