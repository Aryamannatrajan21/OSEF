import yaml
from pathlib import Path
from typing import Any
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.core.ekg import GraphDelta

from .adapters import TrivyAdapter, BanditAdapter


class SecurityEnricher(OsefPlugin):
    def __init__(self):
        manifest_path = Path(__file__).parent.parent / "plugin.yaml"
        with open(manifest_path, "r") as f:
            data = yaml.safe_load(f)
            self._manifest = PluginManifest(**data)

    @property
    def manifest(self) -> PluginManifest:
        return self._manifest

    def activate(self, context: ExtensionContext) -> None:
        context.host.registry.register_enricher(
            name="security_adapters", version=self.manifest.version, factory=self.enrich
        )

    def deactivate(self) -> None:
        pass

    def enrich(self, context: Any, graph: Any) -> GraphDelta:
        delta = GraphDelta()
        # Mock execution of adapters
        trivy = TrivyAdapter()
        delta.nodes_to_add.extend(trivy.parse("dummy").nodes_to_add)

        bandit = BanditAdapter()
        delta.nodes_to_add.extend(bandit.parse("dummy").nodes_to_add)

        return delta
