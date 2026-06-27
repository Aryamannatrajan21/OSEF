from abc import ABC, abstractmethod
from typing import List, Any
from osef.core.ekg import GraphDelta


class InfrastructureAdapter(ABC):
    """
    Base class for adapters that translate native infrastructure models
    into the Infrastructure Knowledge Model (IKM) GraphDelta overlays.
    """

    @abstractmethod
    def parse(self, root_dir: str, **kwargs: Any) -> GraphDelta:
        """
        Parses infrastructure files in the target directory and
        emits a GraphDelta with IKM nodes and edges.
        """
        pass
