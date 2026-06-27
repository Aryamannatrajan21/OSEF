from abc import ABC, abstractmethod
from typing import Any
from osef_visualization.ir import ProjectedGraph


class Renderer(ABC):
    """
    Base class for presenting a ProjectedGraph.
    """

    @abstractmethod
    def get_format(self) -> str:
        pass

    @abstractmethod
    def render(self, graph: ProjectedGraph, **kwargs: Any) -> str:
        pass
