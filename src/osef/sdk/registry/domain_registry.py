from typing import Dict, List, Optional
from osef.sdk.plugin import KnowledgeDomainManifest


class DomainRegistry:
    """Registry for cataloging loaded Knowledge Domains."""

    def __init__(self) -> None:
        self._domains: Dict[str, KnowledgeDomainManifest] = {}

    def register_domain(self, manifest: KnowledgeDomainManifest) -> None:
        """Register a new knowledge domain from a manifest."""
        self._domains[manifest.name] = manifest

    def list_domains(self) -> List[str]:
        """List names of all registered domains."""
        return list(self._domains.keys())

    def get_domain(self, name: str) -> Optional[KnowledgeDomainManifest]:
        """Get a domain manifest by name."""
        return self._domains.get(name)

    def get_node_types(self) -> List[str]:
        """Get all node types across all domains."""
        nodes = []
        for domain in self._domains.values():
            nodes.extend(domain.node_types)
        return list(set(nodes))

    def get_edge_types(self) -> List[str]:
        """Get all edge types across all domains."""
        edges = []
        for domain in self._domains.values():
            edges.extend(domain.edge_types)
        return list(set(edges))

    def get_policy_packs(self) -> List[str]:
        """Get all policy packs across all domains."""
        packs = []
        for domain in self._domains.values():
            packs.extend(domain.policy_packs)
        return list(set(packs))

    def get_adapters(self) -> List[str]:
        """Get all adapters across all domains."""
        adapters = []
        for domain in self._domains.values():
            adapters.extend(domain.adapters)
        return list(set(adapters))

    def get_projections(self) -> List[str]:
        """Get all projections across all domains."""
        projs = []
        for domain in self._domains.values():
            projs.extend(domain.projections)
        return list(set(projs))

    def get_dashboards(self) -> List[str]:
        """Get all dashboards across all domains."""
        dashs = []
        for domain in self._domains.values():
            dashs.extend(domain.dashboards)
        return list(set(dashs))
