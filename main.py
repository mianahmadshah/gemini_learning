from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""
    Analyze this client:

    Name: Ahmad
    Total invoices: 5
    Unpaid invoices: 2
    Outstanding amount: 75000 PKR

    A follow-up is required if there is at least one unpaid invoice.
    """,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "client_name": {
                    "type": "string"
                },
                "unpaid_invoices": {
                    "type": "integer"
                },
                "outstanding_amount": {
                    "type": "integer"
                },
                "requires_followup": {
                    "type": "boolean"
                }
            },
            "required": [
                "client_name",
                "unpaid_invoices",
                "outstanding_amount",
                "requires_followup"
            ]
        }
    )
)

print(response.text)