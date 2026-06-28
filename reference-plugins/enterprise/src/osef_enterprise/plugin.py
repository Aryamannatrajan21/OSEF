"""
Enterprise plugin implementation.
"""

from osef.sdk.plugin import Plugin
from osef.sdk.host.host import ExtensionHost
from osef.sdk.registry.domain_registry import KnowledgeDomainManifest
from osef.core.ekg import GraphDelta, KnowledgeGraph
from osef.sdk.pipeline import PipelineContext
from osef_enterprise.adapters import CodeownersAdapter, OrgChartAdapter
from osef_enterprise.policies import get_all_policies


class EnterpriseEnricher:
    """Runs enterprise adapters."""

    def __call__(self, context: PipelineContext, graph: KnowledgeGraph) -> GraphDelta:
        root = context.workspace_dir
        delta = GraphDelta()

        adapters = [CodeownersAdapter(), OrgChartAdapter()]
        for adapter in adapters:
            d = adapter.parse(root)
            delta.nodes_to_add.extend(d.nodes_to_add)
            delta.edges_to_add.extend(d.edges_to_add)
            delta.diagnostics.extend(d.diagnostics)

        return delta


class EnterprisePlugin(Plugin):
    """
    Registers the Organizational Knowledge Model (OKM).
    """

    def __init__(self):
        super().__init__("osef-enterprise", "1.0.0")

    def register(self, host: "ExtensionHost"):
        manifest = KnowledgeDomainManifest(
            name="Organizational",
            description="Organizational Knowledge Model (OKM) for teams, ownership, and compliance",
            version="1.0.0",
            provides_types=[
                "Organizational.Team",
                "Organizational.Member",
                "Organizational.Role",
                "Organizational.BusinessUnit",
                "Organizational.Product",
                "Organizational.Ownership",
                "Organizational.ServiceCatalog",
                "Compliance.Requirement",
                "Compliance.Framework",
                "Compliance.Control",
            ],
        )
        host.register_domain(manifest)

        # Register Enricher
        host.registry.register_enricher(
            name="enterprise_enricher",
            description="Parses CODEOWNERS and Org Charts",
            factory=EnterpriseEnricher(),
        )

        # Register Policies
        for policy in get_all_policies():
            host.registry.register_policy(policy)

        # Register Dashboards (simulated via reports interface in a real plugin)
        # host.registry.register_report(get_dashboards())
