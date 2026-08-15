from google import genai
import numpy as np

client = genai.Client()

documents = [
    "Employees receive 20 annual leave days.",

    "Invoices are due within 30 days. Clients with unpaid invoices should be contacted after seven additional days.",

    "Projects exceeding their deadline must be reported to management.",

    "Refund requests must be submitted within 14 days."
]
document_embeddings = []

for doc in documents:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=doc
    )

    document_embeddings.append(result.embeddings[0].values)

question = "When should I contact a client who has not paid?"

question_embedding_result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question
)

question_embedding = question_embedding_result.embeddings[0].values
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


scores = []

for embedding in document_embeddings:
    score = cosine_similarity(question_embedding, embedding)
    scores.append(score)


best_index = np.argmax(scores)

retrieved_document = documents[best_index]

print("Question:")
print(question)

print("\nRetrieved Document:")
print(retrieved_document)