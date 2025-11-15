from .improver_agent import ImproverAgent
from llm.llm_client import LLMClient

# Mock input from AssignmentCheckerAgent
payload = {
    "cleaned_text": "Teh cat is on teh mat.\n\nThis is second paragraph."
}

llm_client = LLMClient()
agent = ImproverAgent(llm_client)
result = agent.run(payload)
print(result)
