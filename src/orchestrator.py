from agents.input_agent import InputProcessingAgent
from agents.checker_agent import AssignmentCheckerAgent
from agents.improver_agent import ImproverAgent
from agents.plagiarism_agent import PlagiarismCheckerAgent
from agents.feedback_agent import FeedbackAgent
from llm.llm_client import LLMClient

class Orchestrator:
    def __init__(self):
        # Initialize LLM client
        self.llm_client = LLMClient()

        # Initialize agents
        self.input_agent = InputProcessingAgent()
        self.checker_agent = AssignmentCheckerAgent()
        self.improver_agent = ImproverAgent(self.llm_client)
        self.plagiarism_agent = PlagiarismCheckerAgent()
        self.feedback_agent = FeedbackAgent()

    def run_pipeline(self, text: str, user_id: str = "user123"):
        """
        Run the full SACIA pipeline:
        1. Input processing
        2. Assignment checking
        3. Text improvement
        4. Plagiarism check
        5. Final feedback
        """
        payload = {"text": text}

        # 1️⃣ Input Processing
        processed = self.input_agent.run(payload)

        # 2️⃣ Assignment Checker
        checked = self.checker_agent.run(processed)
        processed.update(checked)

        # 3️⃣ Improver Agent
        improved = self.improver_agent.run(processed)
        processed.update(improved)

        # 4️⃣ Plagiarism Checker
        plag_report = self.plagiarism_agent.run(processed)
        processed.update(plag_report)

        # 5️⃣ Feedback Agent
        final_report = self.feedback_agent.run(processed)

        return final_report

# ✅ Demo run
if __name__ == "__main__":
    orchestrator = Orchestrator()
    sample_text = "Teh cat is on teh mat.\n\nThis is second paragraph."
    report = orchestrator.run_pipeline(sample_text)
    print(report["report"])
