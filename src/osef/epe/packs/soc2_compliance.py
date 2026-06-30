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


class NoHardcodedSecretsRule(Rule):
    @property
    def id(self) -> str:
        return "soc2.security.no_hardcoded_secrets"

    @property
    def version(self) -> str:
        return "1.0.0"

    def evaluate(self, context: RuleContext) -> RuleResult:
        findings = []
        variables = context.get_nodes_by_type("variable")

        for node in variables:
            # A dummy check for hardcoded secrets
            if "password" in node.name.lower() or "secret" in node.name.lower():
                findings.append(
                    Finding(
                        id=f"{self.id}_{node.id}",
                        title=f"Potential Hardcoded Secret: {node.name}",
                        description=f"The variable '{node.name}' may contain a hardcoded secret, violating SOC2 access controls.",
                        severity=Severity.CRITICAL,
                        category=Category.SECURITY,
                        confidence=0.8,
                        provenance=Provenance(
                            rule_id=self.id,
                            rule_version=self.version,
                            policy_version=context.policy_version,
                        ),
                        evidence=Evidence(
                            description="Variable name matches secret patterns.",
                            affected_nodes=[node.id],
                        ),
                        recommendation=Recommendation(
                            action="Use Secrets Manager",
                            description="Move this variable to a secure environment variable or a secrets manager like AWS Secrets Manager or HashiCorp Vault.",
                        ),
                        autofix=AutoFix(available=False),
                    )
                )
        return RuleResult(findings=findings)


soc2_compliance_pack = RulePack(
    id="soc2-compliance-pack",
    version="1.0.0",
    rules=[NoHardcodedSecretsRule()],
)
