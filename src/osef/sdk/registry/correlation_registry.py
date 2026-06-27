from typing import Dict, List
from osef.sdk.correlation import CorrelationRule

class CorrelationRegistry:
    """Registry for cataloging Cross-Domain Correlation Rules."""
    
    def __init__(self):
        self._rules: Dict[str, CorrelationRule] = {}
        
    def register_rule(self, rule: CorrelationRule) -> None:
        """Registers a new correlation rule."""
        if rule.name in self._rules:
            raise ValueError(f"Correlation Rule {rule.name} is already registered.")
        self._rules[rule.name] = rule
        
    def get_rules(self) -> List[CorrelationRule]:
        """Returns all registered correlation rules."""
        return list(self._rules.values())
