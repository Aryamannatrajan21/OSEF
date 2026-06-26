from typing import Dict, List
from osef.epe.core.rule import Rule


class RulePack:
    """
    A collection of rules versioned together.
    """

    def __init__(self, id: str, version: str, rules: List[Rule]):
        self.id = id
        self.version = version
        self.rules = rules


class RuleRegistry:
    """
    Holds registered RulePacks and handles lookups.
    """

    def __init__(self) -> None:
        self.packs: Dict[str, RulePack] = {}
        self.rules_by_id: Dict[str, Rule] = {}

    def register_pack(self, pack: RulePack) -> None:
        self.packs[pack.id] = pack
        for rule in pack.rules:
            self.rules_by_id[rule.id] = rule

    def get_rule(self, rule_id: str) -> Rule:
        if rule_id not in self.rules_by_id:
            raise ValueError(f"Rule {rule_id} not found in registry.")
        return self.rules_by_id[rule_id]
