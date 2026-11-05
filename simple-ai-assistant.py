from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="dummy"
)

response = client.chat.completions.create(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print("ai response:")
print(response.choices[0].message.content)