from .plagiarism_agent import PlagiarismCheckerAgent

# Mock input from ImproverAgent
payload = {
    "improved_text": "[MOCK RESPONSE] Generated text for prompt: Rewrite this text clearly..."
}

agent = PlagiarismCheckerAgent()
result = agent.run(payload)
print(result)

