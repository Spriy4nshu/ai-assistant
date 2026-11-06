from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv();

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["bye", "quit", "exit"]:
        break
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": user_input 
            }
        ]
    )

    print("Aistotle: " + response.choices[0].message.content)