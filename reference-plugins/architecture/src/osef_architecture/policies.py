from typing import List, Any
from osef.core.epe import Finding


class LayeringPolicies:
    name = "architecture_layering"

    def evaluate(self, graph: Any) -> List[Finding]:
        # Mocking drift finding
        return [
            Finding(
                rule_id="ARCH-LAYER-001",
                severity="HIGH",
                message="Domain layer depends on Infrastructure layer (Layering Violation)",
                node_id="Software.Package::domain",
            )
        ]


class DependencyRulesPolicies:
    name = "architecture_dependencies"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


class BoundaryIntegrityPolicies:
    name = "architecture_boundaries"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


class ArchitecturalConstraintsPolicies:
    name = "architecture_constraints"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


class PatternConformancePolicies:
    name = "architecture_patterns"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


class ComponentOwnershipPolicies:
    name = "architecture_ownership"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


class InterfaceCompliancePolicies:
    name = "architecture_interfaces"

    def evaluate(self, graph: Any) -> List[Finding]:
        return []


def get_all_policies() -> list:
    return [
        LayeringPolicies(),
        DependencyRulesPolicies(),
        BoundaryIntegrityPolicies(),
        ArchitecturalConstraintsPolicies(),
        PatternConformancePolicies(),
        ComponentOwnershipPolicies(),
        InterfaceCompliancePolicies(),
    ]
