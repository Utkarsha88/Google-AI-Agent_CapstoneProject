from agents.base_agent import BaseAgent
from llm.llm_client import LLMClient

class AssignmentCheckerAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__("assignment_checker_agent")  # Pass agent name to BaseAgent
        self.llm = LLMClient(api_key)

    def run(self, payload: dict) -> dict:
        """
        payload should contain:
        {
            "text": "assignment text to check"
        }
        """
        text = payload.get("text", "")
        if not text:
            return {"error": "No text provided"}

        # Generate suggestions from Gemini
        try:
            result = self.llm.generate(
                f"Check and improve this assignment text: {text}"
            )
        except Exception as e:
            return {"error": str(e)}

        return {
            "agent_name": self.agent_name,
            "original_text": text,
            "improved_text": result
        }
