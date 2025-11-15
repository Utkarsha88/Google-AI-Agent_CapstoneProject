from .base_agent import BaseAgent
from llm.llm_client import LLMClient

class ImproverAgent(BaseAgent):
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def run(self, payload: dict) -> dict:
        """
        Improve the assignment text using LLM.
        Returns improved text and a changelog.
        """
        text = payload.get("cleaned_text", "")
        
        # Create a prompt for the LLM
        prompt = f"Rewrite this text clearly and fix grammar: {text}"
        
        # Get LLM response (mock for now)
        response = self.llm.generate(prompt)
        improved_text = response.get("text", text)
        
        # Simple changelog example
        changelog = [
            {
                "location": "sentence 1",
                "before": text,
                "after": improved_text
            }
        ]
        
        return {
            "improved_text": improved_text,
            "changelog": changelog
        }
