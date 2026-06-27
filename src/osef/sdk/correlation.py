from typing import Protocol, runtime_checkable, Any
from osef.core.ekg import KnowledgeGraph

@runtime_checkable
class CorrelationRule(Protocol):
    """Protocol for rules that execute in the Correlation Engine."""
    
    @property
    def name(self) -> str:
        """Name of the correlation rule."""
        ...
        
    @property
    def description(self) -> str:
        """Description of what this rule correlates."""
        ...
        
    def evaluate(self, graph: KnowledgeGraph) -> Any:
        """
        Evaluate the rule against the graph and return a GraphDelta.
        Returns Any (GraphDelta) to avoid circular imports.
        """
        ...
