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

# Example inference request
response = client.complete(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    model="your-model-name"
)

print(response.choices[0].message.content)
