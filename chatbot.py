from google import genai

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    response = chat.send_message(user_message)

    print("Gemini:", response.text)

    print("\n--- HISTORY ---")
    for message in chat.get_history():
        print(message)
    print("----------------\n")