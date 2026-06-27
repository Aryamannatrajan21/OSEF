from typing import Any
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.core.ekg import KnowledgeGraph, GraphDelta, Edge

import yaml
from pathlib import Path

class DeployedAsRule:
    name = "software_deployed_as_infrastructure"
    description = "Correlates Software.Service nodes with Infrastructure.Container nodes."
    
    def evaluate(self, graph: KnowledgeGraph) -> GraphDelta:
        delta = GraphDelta()
        services = [n for n in graph.get_nodes() if n.type == "Software.Service"]
        containers = [n for n in graph.get_nodes() if n.type == "Infrastructure.Container"]
        
        for service in services:
            for container in containers:
                # Basic heuristic matching on name
                if service.name in container.name or container.name in service.name:
                    delta.edges_to_add.append(Edge(
                        source_id=service.id,
                        target_id=container.id,
                        relation_type="DEPLOYED_AS"
                    ))
        
        return delta

class CrossDomainIntelligencePlugin(OsefPlugin):
    
    def __init__(self):
        manifest_path = Path(__file__).parent.parent / "plugin.yaml"
        with open(manifest_path, 'r') as f:
            data = yaml.safe_load(f)
            self._manifest = PluginManifest(**data)
            
    @property
    def manifest(self) -> PluginManifest:
        return self._manifest
        
    def activate(self, context: ExtensionContext) -> None:
        rule = DeployedAsRule()
        context.host.correlation_registry.register_rule(rule)
        
    def deactivate(self) -> None:
        pass
