from abc import ABC, abstractmethod
from typing import Any
from osef.sdk.queries import GraphQuery
from osef_visualization.ir import ProjectedGraph


class Projection(ABC):
    """
    Base class for an Engineering View of the Graph.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def project(self, query: GraphQuery, **kwargs: Any) -> ProjectedGraph:
        pass
