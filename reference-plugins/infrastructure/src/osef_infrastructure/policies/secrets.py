from typing import List, Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM


def check_secrets_in_env_vars(graph: KnowledgeGraph) -> List[Dict[str, Any]]:
    violations = []
    for node in graph.get_nodes():
        if node.type == IKM.IMAGE:
            env_vars = node.metadata.get("env_vars", "")
            if "PASSWORD" in env_vars.upper() or "SECRET" in env_vars.upper():
                violations.append(
                    {
                        "policy": "SecretsInEnvVars",
                        "severity": "CRITICAL",
                        "node_id": node.id,
                        "message": "Potential secret exposed in Dockerfile ENV instructions.",
                    }
                )
    return violations


def get_secrets_policies() -> List[Any]:
    return [check_secrets_in_env_vars]
