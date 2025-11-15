from .checker_agent import AssignmentCheckerAgent

# Mock input from InputProcessingAgent
payload = {
    "cleaned_text": "Teh cat is on teh mat.\n\nThis is second paragraph."
}

agent = AssignmentCheckerAgent()
result = agent.run(payload)
print(result)
