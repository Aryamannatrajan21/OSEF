from abc import ABC, abstractmethod
from typing import List
from osef.epe.core.context import RuleContext
from osef.epe.core.result import RuleResult


class Rule(ABC):
    """
    Abstract base class for all Engineering Policies.
    """

    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def id(self) -> str:
        """Unique ID of the rule, e.g. osef.core.arch.no_god_objects"""
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """Version string, e.g. 1.0.0"""
        pass

    @property
    def dependencies(self) -> List[str]:
        """IDs of rules that must run before this rule."""
        return []

    @abstractmethod
    def evaluate(self, context: RuleContext) -> RuleResult:
        """Executes the rule against the Graph via the RuleContext."""
        pass
