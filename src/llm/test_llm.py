from llm_client import LLMClient

client = LLMClient()
prompt = "Rewrite this sentence to make it clearer: Teh cat is on teh mat."
response = client.generate(prompt)
print(response["text"])
