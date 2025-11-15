from .base_agent import BaseAgent

class InputProcessingAgent(BaseAgent):
    def run(self, payload: dict) -> dict:
        """
        Process raw assignment text.
        Returns structured JSON.
        """
        text = payload.get("text", "")
        # Clean text
        cleaned_text = text.strip()
        # Split paragraphs by double newline
        paragraphs = cleaned_text.split("\n\n")
        # Mock assignment type and language detection
        assignment_type = "essay"
        language = "en"

        return {
            "cleaned_text": cleaned_text,
            "paragraphs": paragraphs,
            "assignment_type": assignment_type,
            "language": language
        }
