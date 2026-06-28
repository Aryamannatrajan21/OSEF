"""
Ecosystem Registry.
"""
from typing import Dict, List, Optional
from osef.sdk.plugin import PluginManifest
from osef.sdk.registry.domain_registry import KnowledgeDomainManifest
from osef.sdk.profiles.profile import EngineeringProfile
from osef.sdk.profiles.registry import get_default_profiles
from osef.sdk.registry.compatibility import CompatibilityEngine


class EcosystemRegistry:
    """
    The single source of truth for the entire OSEF ecosystem.
    """
    def __init__(self):
        self.plugins: Dict[str, PluginManifest] = {}
        self.domains: Dict[str, KnowledgeDomainManifest] = {}
        self.profiles: Dict[str, EngineeringProfile] = get_default_profiles()
        self.compatibility = CompatibilityEngine()

    def register_plugin(self, manifest: PluginManifest):
        self.compatibility.check_plugin(manifest)
        self.plugins[manifest.id] = manifest
        if manifest.knowledge_domain:
            self.domains[manifest.knowledge_domain.name] = manifest.knowledge_domain

    def get_plugin(self, plugin_id: str) -> Optional[PluginManifest]:
        return self.plugins.get(plugin_id)

    def list_plugins(self) -> List[PluginManifest]:
        return list(self.plugins.values())

    def list_domains(self) -> List[KnowledgeDomainManifest]:
        return list(self.domains.values())

    def list_profiles(self) -> List[EngineeringProfile]:
        return list(self.profiles.values())
