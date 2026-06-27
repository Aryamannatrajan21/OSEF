from typing import List, Any
from osef.core.ekg import KnowledgeGraph, GraphDelta
from osef.sdk.pipeline import PipelineContext
from osef_infrastructure.adapters import DockerAdapter, ComposeAdapter, KubernetesAdapter
from osef_infrastructure.policies import get_all_policies
from osef_infrastructure.projections import get_projections

class InfrastructureEnricher:
    """Provides semantic enrichment for infrastructure configuration."""
    def __call__(self, context: PipelineContext, graph: KnowledgeGraph) -> GraphDelta:
        root = context.workspace_dir
        delta = GraphDelta()
        
        # Run all adapters
        adapters = [
            DockerAdapter(),
            ComposeAdapter(),
            KubernetesAdapter()
        ]
        
        for adapter in adapters:
            d = adapter.parse(root)
            delta.nodes_to_add.extend(d.nodes_to_add)
            delta.edges_to_add.extend(d.edges_to_add)
            delta.diagnostics.extend(d.diagnostics)
            
        return delta

class InfrastructurePolicyPack:
    """Provides infrastructure engineering policies."""
    def __call__(self) -> List[Any]:
        return get_all_policies()

from osef_infrastructure.cli import InfraCliCommand

class InfrastructureCli:
    """Provides infrastructure CLI commands."""
    def __call__(self, *args, **kwargs) -> Any:
        return InfraCliCommand()

from osef_infrastructure.dashboards import get_dashboards

class InfrastructureReports:
    """Provides infrastructure dashboards/reports."""
    def __call__(self, *args, **kwargs) -> Any:
        return get_dashboards()

class InfrastructureProjections:
    """Provides infrastructure projections to the Capability Registry."""
    def __call__(self) -> dict:
        return get_projections()
