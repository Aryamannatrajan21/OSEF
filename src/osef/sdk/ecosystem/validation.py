import os
from typing import List, Dict
from osef.sdk.ecosystem.registry import EcosystemRegistry

class PlatformValidationEngine:
    """
    Runs the full pipeline across all files in a workspace dynamically by looking up
    the LanguageCapability via the EcosystemRegistry.
    Never knows about specific language packs.
    """
    def __init__(self, registry: EcosystemRegistry):
        self.registry = registry
        
    def validate_workspace(self, workspace_path: str, profiles: List[str] = None):  # type: ignore
        print(f"Starting Platform Validation on {workspace_path}")
        
        # In a real environment, this would walk the directory. For now, simulate.
        files = []
        for root, dirs, filenames in os.walk(workspace_path):
            for f in filenames:
                files.append(os.path.join(root, f))
                
        # Filter files by profiles if active
        active_pipelines = set()
        if profiles:
            for p in profiles:
                active_pipelines.update(self.registry.get_pipelines_for_profile(p))
                
        graph_deltas = []
        
        for filepath in files:
            try:
                pipeline = self.registry.get_pipeline_for_file(filepath)
                if profiles and pipeline not in active_pipelines:
                    continue # Skip files not in active profiles
                
                print(f"  Validating {filepath} using generic LanguageCapability...")
                
                ast = pipeline.parse(filepath)
                symbols = pipeline.extract_symbols(ast)
                resolved = pipeline.resolve(symbols)  # type: ignore
                facts = pipeline.analyze(resolved)  # type: ignore
                delta = pipeline.map_to_graph(facts)  # type: ignore
                
                graph_deltas.append(delta)
            except ValueError:
                pass # Unregistered file extension
                
        print(f"Validation complete. Generated {len(graph_deltas)} GraphDeltas.")
        return graph_deltas
