import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve endpoint and key
endpoint = os.getenv("AZURE_AI_ENDPOINT")
key = os.getenv("AZURE_AI_KEY")

# Initialize the client
client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Initialize the conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Start the conversation (type 'exit' to end):")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    messages.append({"role": "user", "content": user_input})

    response = client.complete(
        messages=messages,
        model="Phi-3-small-8k-instruct"
    )

    assistant_response = response.choices[0].message.content
    print(f"Assistant: {assistant_response}")

    messages.append({"role": "assistant", "content": assistant_response})
