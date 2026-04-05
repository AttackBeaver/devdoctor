from abc import ABC, abstractmethod

class Check(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self) -> tuple[bool, str]:
        """Returns (success, message)"""
        pass

    @abstractmethod
    def fix(self) -> bool:
        """Attempts to fix the issue. Returns True if fixed."""
        pass
