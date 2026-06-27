import yaml
from pathlib import Path
from typing import Any
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.core.ekg import GraphDelta

from .adapters import C4ModelAdapter, OsefArchitectureAdapter, ADRAdapter
from .policies import get_all_policies
from .projections import get_projections
from .dashboards import get_dashboards
from .correlations import get_correlation_rules

class ArchitectureEnricher(OsefPlugin):
    
    def __init__(self):
        manifest_path = Path(__file__).parent.parent / "plugin.yaml"
        with open(manifest_path, 'r') as f:
            data = yaml.safe_load(f)
            self._manifest = PluginManifest(**data)
            
    @property
    def manifest(self) -> PluginManifest:
        return self._manifest
        
    def activate(self, context: ExtensionContext) -> None:
        context.host.registry.register_enricher(
            name="architecture_adapters",
            version=self.manifest.version,
            factory=self.enrich
        )
        
        # Architecture Domain contributes correlation rules to the engine
        for rule in get_correlation_rules():
            context.host.correlation_registry.register_rule(rule)
            
    def deactivate(self) -> None:
        pass
        
    def enrich(self, context: Any, graph: Any) -> GraphDelta:
        delta = GraphDelta()
        
        c4 = C4ModelAdapter()
        delta.nodes_to_add.extend(c4.parse("dummy").nodes_to_add)
        
        osef_arch = OsefArchitectureAdapter()
        delta.nodes_to_add.extend(osef_arch.parse("dummy").nodes_to_add)
        
        adr = ADRAdapter()
        delta.nodes_to_add.extend(adr.parse("dummy").nodes_to_add)
        
        return delta
