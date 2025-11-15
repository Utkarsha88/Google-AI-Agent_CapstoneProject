from .feedback_agent import FeedbackAgent

# Mock input from PlagiarismCheckerAgent
payload = {
    "issues": [
        {"type": "grammar", "location": "sentence 1", "explanation": "Spelling error: should be 'The cat'"}
    ],
    "improved_text": "[MOCK RESPONSE] Generated text for prompt: Rewrite this text clearly...",
    "plagiarism_percentage": 10,
    "score": 75
}

agent = FeedbackAgent()
result = agent.run(payload)
print(result["report"])
