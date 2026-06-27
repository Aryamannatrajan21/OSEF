from osef.sdk.plugin import Plugin
from osef.sdk.registry.domain_registry import KnowledgeDomainManifest
from runtime.rkm import RuntimeKnowledgeModel
from runtime.adapters import OsefRuntimeYamlAdapter
from runtime.correlations import RuntimeCorrelations
from runtime.policies import RuntimePolicies
from runtime.projections import RuntimeProjections

class RuntimePlugin(Plugin):
    """
    OSEF Runtime Knowledge Domain Plugin.
    Models deterministic execution behavior independent of deployment topology.
    """
    def __init__(self):
        super().__init__("osef-runtime", "1.0.0")

    def register(self, host: "ExtensionHost"):
        manifest = KnowledgeDomainManifest(
            name="Runtime",
            description="Models execution behavior (Processes, Threads, Traces).",
            nodes=RuntimeKnowledgeModel.get_schema(),
            adapters=[OsefRuntimeYamlAdapter],
            correlations=RuntimeCorrelations.get_rules(),
            policies=RuntimePolicies.get_rules(),
            projections=RuntimeProjections.get_projections()
        )
        host.domain_registry.register(manifest)
