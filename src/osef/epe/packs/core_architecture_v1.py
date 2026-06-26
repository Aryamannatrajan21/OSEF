from osef.epe.core.rule import Rule
from osef.epe.core.context import RuleContext
from osef.epe.core.result import (
    RuleResult,
    Finding,
    Provenance,
    Evidence,
    Recommendation,
    AutoFix,
)
from osef.epe.core.severity import Severity
from osef.epe.core.category import Category
from osef.epe.core.registry import RulePack


class MissingDocumentationRule(Rule):
    @property
    def id(self) -> str:
        return "osef.core.doc.missing_doc"

    @property
    def version(self) -> str:
        return "1.0.0"

    def evaluate(self, context: RuleContext) -> RuleResult:
        findings = []
        funcs = context.get_nodes_by_type("function") + context.get_nodes_by_type(
            "method"
        )
        classes = context.get_nodes_by_type("class")

        for node in funcs + classes:
            if not node.description:
                findings.append(
                    Finding(
                        id=f"{self.id}_{node.id}",
                        title=f"Missing Documentation on {node.name}",
                        description=f"The {node.type} '{node.name}' is missing a docstring.",
                        severity=Severity.LOW,
                        category=Category.DOCUMENTATION,
                        confidence=1.0,
                        provenance=Provenance(
                            rule_id=self.id,
                            rule_version=self.version,
                            policy_version=context.policy_version,
                        ),
                        evidence=Evidence(
                            description="Node description is empty.",
                            affected_nodes=[node.id],
                        ),
                        recommendation=Recommendation(
                            action="Add docstring",
                            description=f"Add a PEP-257 compliant docstring to {node.name}.",
                        ),
                        autofix=AutoFix(available=False),
                    )
                )
        return RuleResult(findings=findings)


class UnresolvedImportsRule(Rule):
    @property
    def id(self) -> str:
        return "osef.core.dep.unresolved_imports"

    @property
    def version(self) -> str:
        return "1.0.0"

    def evaluate(self, context: RuleContext) -> RuleResult:
        findings = []
        for node in context.get_nodes_by_type("import"):
            if node.metadata.get("resolved") != "true":
                findings.append(
                    Finding(
                        id=f"{self.id}_{node.id}",
                        title=f"Unresolved Import: {node.name}",
                        description=f"The import '{node.name}' could not be resolved to a local module.",
                        severity=Severity.MEDIUM,
                        category=Category.DEPENDENCIES,
                        confidence=1.0,
                        provenance=Provenance(
                            rule_id=self.id,
                            rule_version=self.version,
                            policy_version=context.policy_version,
                        ),
                        evidence=Evidence(
                            description="Import node lacks 'resolved=true' metadata.",
                            affected_nodes=[node.id],
                        ),
                        recommendation=Recommendation(
                            action="Verify dependency",
                            description="Ensure the module is installed or path is correct.",
                        ),
                    )
                )
        return RuleResult(findings=findings)


core_architecture_pack_v1 = RulePack(
    id="osef-core-architecture",
    version="1.0.0",
    rules=[MissingDocumentationRule(), UnresolvedImportsRule()],
)
