from typing import List
from osef.epe.core.rule import Rule
from osef.epe.core.context import RuleContext
from osef.epe.core.result import RuleResult, Finding
from osef.epe.core.severity import FindingSeverity


class MissingReadmeRule(Rule):
    @property
    def id(self) -> str:
        return "osef.docs.missing_readme"

    @property
    def version(self) -> str:
        return "1.0.0"

    def evaluate(self, context: RuleContext) -> RuleResult:
        findings = []
        if "doc:README.md" not in context.graph.nodes:
            findings.append(
                Finding(
                    rule_id=self.id,
                    severity=FindingSeverity.ERROR,
                    message="Repository is missing a root README.md",
                    target_node_id=None,
                )
            )
        return RuleResult(rule_id=self.id, passed=len(findings) == 0, findings=findings)


class ArchitectureDriftRule(Rule):
    @property
    def id(self) -> str:
        return "osef.docs.architecture_drift"

    @property
    def version(self) -> str:
        return "1.0.0"

    def evaluate(self, context: RuleContext) -> RuleResult:
        # A mock implementation that checks if any code refers to architecture incorrectly
        # Or if architecture is undocumented
        return RuleResult(rule_id=self.id, passed=True, findings=[])


def get_documentation_policies() -> List[Rule]:
    return [MissingReadmeRule(), ArchitectureDriftRule()]
