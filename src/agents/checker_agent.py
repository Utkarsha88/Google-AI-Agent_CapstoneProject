from .base_agent import BaseAgent

class AssignmentCheckerAgent(BaseAgent):
    def run(self, payload: dict) -> dict:
        """
        Check assignment for grammar, clarity, and logical issues.
        Returns a JSON with issues and a score.
        """
        text = payload.get("cleaned_text", "")
        
        # Mock example: pretend we found a grammar issue
        issues = [
            {
                "type": "grammar",
                "location": "sentence 1",
                "original": "Teh cat",
                "explanation": "Spelling error: should be 'The cat'"
            }
        ]
        
        # Mock score out of 100
        score = 75
        
        return {
            "issues": issues,
            "score": score
        }
