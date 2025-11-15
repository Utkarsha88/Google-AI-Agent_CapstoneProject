from llm_client import LLMClient

API_KEY = "your_api_key_here"

client = LLMClient(api_key=API_KEY)

prompt = "Explain quantum computing in simple language."
result = client.generate(prompt)

print("MODEL RESPONSE:\n", result)
