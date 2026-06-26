"""
Engineering Pipeline Engine.
Orchestrates capability-driven execution.
"""

import logging
from pathlib import Path

from osef.core.ekg import KnowledgeGraph, Node, Edge
from osef.scanner.scanner import RepositoryScanner
from osef.sdk.host.host import ExtensionHost
from osef.sdk.pipeline import PipelineContext
from osef.sdk.events import EventType

# Fallback imports (Strangler Migration)
from osef.parser.python import PythonParser as LegacyPythonParser
from osef.parser.symbol_table import SymbolTable
from osef.parser.resolvers.imports import ImportResolver
from osef.parser.resolvers.types import TypeResolver
from osef.semantic.enrichers import SemanticEnricher
from osef.config.parser import ConfigParser

logger = logging.getLogger(__name__)


class PipelineEngine:
    """
    Orchestrates execution stages using capabilities resolved by the ExtensionHost.
    """

    def __init__(self, root_path: str | Path, host: ExtensionHost = None):
        self.root_path = Path(root_path).resolve()
        self.graph = KnowledgeGraph()
        
        # If host is not provided (legacy usage), we instantiate an empty one.
        self.host = host or ExtensionHost(self.root_path, self.graph)
        self.event_bus = self.host.event_bus

    def build(self) -> KnowledgeGraph:
        """
        Execute the Engineering Pipeline.
        """
        # --- STAGE: Scanning ---
        self.event_bus.publish(EventType.BeforeRepositoryScan, {"path": str(self.root_path)})
        scanner = RepositoryScanner(self.root_path)
        manifest = scanner.scan()
        self.event_bus.publish(EventType.AfterRepositoryScan, {"files_count": len(manifest.python_files)})

        # Create PipelineContext
        context = PipelineContext(
            manifest=manifest,
            workspace_dir=self.root_path,
            extension_context=None, # TBD: Maybe we don't need a specific plugin's context here
        )

        # --- STAGE: Parsing ---
        self.event_bus.publish(EventType.BeforeParsing, {})
        
        symbol_table = None
        
        # Resolve Capability
        parser_cap = self.host.registry.resolve_parser(language="python")
        
        if parser_cap:
            logger.info("Executing parsing via python capability factory")
            symbol_table = parser_cap.factory(context)
        else:
            logger.warning("No parser plugin found for Python. Falling back to LegacyPythonParser.")
            symbol_table = SymbolTable()
            parser = LegacyPythonParser(symbol_table)
            for python_file in manifest.python_files:
                abs_path = self.root_path / python_file
                parser.parse_file(str(abs_path))
                
        # Parse configs (still legacy for now)
        config_parser = ConfigParser(self.root_path, symbol_table)
        config_parser.parse_all()
        
        self.event_bus.publish(EventType.AfterParsing, {"symbols_count": len(symbol_table.symbols)})

        # --- STAGE: Semantic Enrichment ---
        self.event_bus.publish(EventType.BeforeSemanticEnrichment, {})
        
        # Legacy resolvers for now until we extract semantic capability
        import_resolver = ImportResolver(symbol_table)
        import_resolver.resolve()

        type_resolver = TypeResolver(symbol_table)
        type_resolver.resolve()

        enricher = SemanticEnricher(symbol_table)
        enricher.enrich()
        
        self.event_bus.publish(EventType.AfterSemanticEnrichment, {})

        # --- STAGE: Graph Construction ---
        self.event_bus.publish(EventType.BeforeGraphGeneration, {})
        
        for symbol in symbol_table.symbols.values():
            node = Node(
                id=symbol.id,
                type=symbol.type,
                name=symbol.name,
                description=symbol.docstring,
                metadata={
                    "file_path": symbol.file_path,
                    "visibility": symbol.visibility,
                    **symbol.metadata,
                },
            )
            self.graph.add_node(node)

        for symbol in symbol_table.symbols.values():
            for child_id in symbol.children_ids:
                self.graph.add_edge(Edge(source_id=symbol.id, target_id=child_id, relation_type="CONTAINS"))

            if symbol.type == "import" and symbol.metadata.get("resolved") == "true":
                target_id = symbol.metadata.get("resolved_to")
                if target_id:
                    self.graph.add_edge(Edge(source_id=symbol.id, target_id=target_id, relation_type="IMPORTS"))

            for callee_id in symbol.related_ids.get("CALLS", []):
                self.graph.add_edge(Edge(source_id=symbol.id, target_id=callee_id, relation_type="CALLS"))

        if not self.graph.validate_graph():
            raise RuntimeError("Generated EKG is invalid (dangling edges).")
            
        self.event_bus.publish(EventType.AfterGraphGeneration, {"nodes": len(self.graph.nodes), "edges": len(self.graph.edges)})
        
        # --- STAGE: Graph Enrichment ---
        enrichers = self.host.registry.get_enrichers()
        for enricher_cap in enrichers:
            logger.info(f"Executing enrichment via {enricher_cap.name}")
            delta = enricher_cap.factory(context, self.graph)
            
            # Validate and merge the delta back into the graph
            if not delta.validate(self.graph):
                logger.error(f"GraphDelta validation failed from {enricher_cap.name}: {delta.diagnostics}")
                continue
                
            provenance = {
                "plugin": self.host.registry._plugin_mapping.get(enricher_cap, "unknown"),
                "execution_id": "pipeline_run", # Could be dynamic UUID in future
            }
            self.graph.merge_delta(delta, provenance)
            logger.info(f"Merged GraphDelta from {enricher_cap.name}: +{len(delta.nodes_to_add)} nodes, +{len(delta.edges_to_add)} edges")

        return self.graph

# Alias for backward compatibility
EKGBuilder = PipelineEngine
