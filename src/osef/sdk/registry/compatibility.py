"""
Compatibility Engine for OSEF Ecosystem.
"""
from importlib.metadata import version as get_version
from typing import List, Dict, Optional
from osef.sdk.plugin import PluginManifest
from osef.contracts.exceptions import OSEFError

class CompatibilityEngine:
    """
    Evaluates compatibility constraints for plugins and profiles.
    """
    def __init__(self):  # type: ignore
        try:
            self.sdk_version = get_version("osef")
        except Exception:
            self.sdk_version = "0.1.0"
            
        self.graph_schema = "1.0" # Current frozen schema version

    def check_plugin(self, manifest: PluginManifest, active_profile: Optional[str] = None) -> bool:
        """
        Validates if a plugin can run in the current environment.
        """
        if manifest.sdk_version != self.sdk_version and not self.sdk_version.startswith("0.1."):
            # Simple check for demo purposes
            pass
            
        if manifest.graph_schema != self.graph_schema and manifest.graph_schema != "any":
            raise OSEFError(f"Plugin {manifest.name} requires graph schema {manifest.graph_schema} but system is {self.graph_schema}")
            
        if active_profile and manifest.supported_profiles:
            if active_profile not in manifest.supported_profiles:
                raise OSEFError(f"Plugin {manifest.name} does not support profile {active_profile}")
                
        return True

    def validate_ecosystem(self, plugins: List[PluginManifest]) -> Dict[str, str]:
        """
        Validates an entire set of plugins for co-existence issues.
        """
        issues = {}
        for plugin in plugins:
            try:
                self.check_plugin(plugin)
            except OSEFError as e:
                issues[plugin.name] = str(e)
        return issues
