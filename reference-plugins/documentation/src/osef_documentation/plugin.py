import yaml
import logging
from pathlib import Path
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.sdk.capabilities import GraphEnrichmentCapability, PolicyCapability, ReportCapability, CLIExtensionCapability
from osef_documentation.enricher import DocumentationEnricher
from osef_documentation.policies import get_documentation_policies

logger = logging.getLogger(__name__)

class DocumentationPlugin(OsefPlugin):
    """
    The official Documentation Intelligence reference implementation.
    Validates GraphEnrichment Capabilities.
    """
    @property
    def manifest(self) -> PluginManifest:
        yaml_path = Path(__file__).parent.parent.parent / "plugin.yaml"
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        return PluginManifest(**data)

    def activate(self, context: ExtensionContext) -> None:
        """
        Register capabilities into the ExtensionContext.
        """
        enricher = DocumentationEnricher()
        
        cap = GraphEnrichmentCapability(
            name="DocumentationEnrichment",
            factory=enricher.enrich,
            stage="after_graph_build",
            priority=100,
            dependencies=["parser"],
            produces=["documentation_layer"]
        )
        context.register_capability(cap)
        
        # Policy Capability
        policy_cap = PolicyCapability(
            name="DocumentationPolicies",
            factory=get_documentation_policies
        )
        context.register_capability(policy_cap)
        
        # Report Capability
        report_cap = ReportCapability(
            name="DocumentationCoverageReport",
            factory=lambda: {"report_type": "documentation_coverage", "data": "TBD"}
        )
        context.register_capability(report_cap)
        
        # CLI Capability
        def cli_docs():
            print("Running osef docs command")
            
        cli_cap = CLIExtensionCapability(
            command_name="docs",
            factory=cli_docs
        )
        context.register_capability(cli_cap)

    def deactivate(self) -> None:
        pass
