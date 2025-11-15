from .base_agent import BaseAgent

class FeedbackAgent(BaseAgent):
    def run(self, payload: dict) -> dict:
        """
        Generate a final assignment report combining all previous outputs.
        """
        issues = payload.get("issues", [])
        improved_text = payload.get("improved_text", "")
        plagiarism = payload.get("plagiarism_percentage", 0)
        base_score = payload.get("score", 0)

        # Adjust score based on plagiarism (simple mock logic)
        final_score = max(base_score - plagiarism / 2, 0)

        # Create a report string
        report = f"# Assignment Report\n"
        report += f"Final Score: {final_score}\n"
        report += f"Plagiarism: {plagiarism}%\n"
        report += f"Improved Text:\n{improved_text}\n"
        report += f"Issues:\n"
        for issue in issues:
            report += f"- {issue['type']} at {issue['location']}: {issue['explanation']}\n"

        return {
            "report": report,
            "final_score": final_score,
            "final_text": improved_text
        }
