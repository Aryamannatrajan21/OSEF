import json
from typing import Dict, Any, List
from src.osef.sdk.language.pipeline import LanguagePipeline

class PluginManifest:
    def __init__(self, data: Dict[str, Any]):
        self.language = data.get("language")
        self.quality_tier = data.get("quality_tier")
        self.supported_extensions = data.get("supported_file_extensions", [])
        self.supported_profiles = data.get("supported_profiles", [])

class EcosystemRegistry:
    """
    Central registry for OSEF Language Packs.
    No hardcoded logic for specific languages.
    """
    def __init__(self):
        self.plugins: Dict[str, PluginManifest] = {}
        self.pipelines: Dict[str, LanguagePipeline] = {}
        
    def register_plugin(self, manifest_path: str, pipeline: LanguagePipeline):
        with open(manifest_path, "r") as f:
            data = json.load(f)
        manifest = PluginManifest(data)
        self.plugins[manifest.language] = manifest
        self.pipelines[manifest.language] = pipeline
        
    def get_pipeline_for_file(self, filepath: str) -> LanguagePipeline:
        for lang, manifest in self.plugins.items():
            for ext in manifest.supported_extensions:
                if filepath.endswith(ext):
                    return self.pipelines[lang]
        raise ValueError(f"No registered language pack supports file: {filepath}")

    def get_pipelines_for_profile(self, profile: str) -> List[LanguagePipeline]:
        matched = []
        for lang, manifest in self.plugins.items():
            if profile in manifest.supported_profiles:
                matched.append(self.pipelines[lang])
        return matched
