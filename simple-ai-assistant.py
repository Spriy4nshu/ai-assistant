from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv();

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages = []
messages.extend([
    {
        "role": "system",
        "content": "You are a smart scientist with extensive knowledge of almost everything",
    },
    {
        "role": "system",
        "content": "Keep your responses to less than 100 words."
    },
    {
        "role": "system",
        "content": "If you don't know the answer, say 'I don't know.'",
    },
    {
        
        "role": "system",
        "content": "make sure you explain as someone who is a begineer until you give enough context for advance knowledge"
    }]
)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["bye", "quit", "exit"]:
        break
        
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )

    print("Aristotle: " + response.choices[0].message.content)