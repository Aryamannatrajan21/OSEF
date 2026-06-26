from abc import ABC, abstractmethod
from typing import Dict, Any

class ReportTarget(ABC):
    """
    Extensible reporting interface. (e.g. Markdown, SARIF, JSON, HTML)
    """
    @abstractmethod
    def generate(self, assessment: Dict[str, Any]) -> str:
        pass
