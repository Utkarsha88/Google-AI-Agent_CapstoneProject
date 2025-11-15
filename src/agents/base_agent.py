from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, agent_name: str):
        self.agent_name = agent_name

    @abstractmethod
    def run(self, payload: dict) -> dict:
        """Process payload and return structured JSON result."""
        pass
