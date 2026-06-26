from typing import List, Set
from osef.core.ekg import KnowledgeGraph
from osef.epe.core.registry import RuleRegistry
from osef.epe.core.context import RuleContext
from osef.epe.core.result import Finding
from osef.epe.core.rule import Rule


class PolicyEngine:
    """
    Orchestrates execution by resolving rule dependencies via a DAG, executing rules, and collecting findings.
    """
    def __init__(self, registry: RuleRegistry, policy_version: str):
        self.registry = registry
        self.policy_version = policy_version

    def evaluate(self, graph: KnowledgeGraph) -> List[Finding]:
        context = RuleContext(graph, self.policy_version)
        all_findings: List[Finding] = []
        
        # Sort rules via DAG
        ordered_rules = self._topological_sort(list(self.registry.rules_by_id.values()))
        
        for rule in ordered_rules:
            result = rule.evaluate(context)
            all_findings.extend(result.findings)
            
        return all_findings

    def _topological_sort(self, rules: List[Rule]) -> List[Rule]:
        # Basic topological sort
        visited: Set[str] = set()
        temp_mark: Set[str] = set()
        ordered: List[Rule] = []

        def visit(rule_id: str) -> None:
            if rule_id in temp_mark:
                raise ValueError(f"Circular dependency detected involving rule {rule_id}")
            if rule_id not in visited:
                temp_mark.add(rule_id)
                rule = self.registry.get_rule(rule_id)
                for dep in rule.dependencies:
                    visit(dep)
                temp_mark.remove(rule_id)
                visited.add(rule_id)
                ordered.append(rule)

        for rule in rules:
            if rule.id not in visited:
                visit(rule.id)
                
        return ordered
