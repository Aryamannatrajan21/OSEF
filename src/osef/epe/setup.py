from osef.epe.core.registry import RuleRegistry
from osef.epe.core.engine import PolicyEngine
from osef.epe.packs.core_architecture_v1 import core_architecture_pack_v1


def get_default_engine() -> PolicyEngine:
    registry = RuleRegistry()
    registry.register_pack(core_architecture_pack_v1)
    return PolicyEngine(registry=registry, policy_version="1.0.0")
