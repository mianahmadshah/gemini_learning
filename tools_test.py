from google import genai
from google.genai import types

client = genai.Client()

clients = {
    "Ahmad": 75000,
    "Ali": 25000,
    "Sara": 0
}

def get_client_balance(client_name: str) -> int:
    """Get the outstanding balance of a client in PKR."""
    return clients.get(client_name, 0)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How much does Ali owe?",
    config=types.GenerateContentConfig(
        tools=[get_client_balance]
    )
)

print(response.text)