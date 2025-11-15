from .input_agent import InputProcessingAgent

agent = InputProcessingAgent()
sample_text = "Teh cat is on teh mat.\n\nThis is second paragraph."
payload = {"text": sample_text}

result = agent.run(payload)
print(result)
