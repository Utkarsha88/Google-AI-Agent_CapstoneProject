from .base_agent import BaseAgent

class PlagiarismCheckerAgent(BaseAgent):
    def run(self, payload: dict) -> dict:
        """
        Check improved text for plagiarism.
        Returns plagiarism percentage and suspicious lines.
        """
        text = payload.get("improved_text", "")
        
        # Mock plagiarism check
        plagiarism_percentage = 10  # 10% plagiarized
        matched_sources = ["https://example.com/source1"]
        suspicious_lines = ["sentence 1"]
        rephrase_suggestions = ["Rewrite sentence 1 for originality"]
        
        return {
            "plagiarism_percentage": plagiarism_percentage,
            "matched_sources": matched_sources,
            "suspicious_lines": suspicious_lines,
            "rephrase_suggestions": rephrase_suggestions
        }
