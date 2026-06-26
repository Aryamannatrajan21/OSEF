"""
Engineering Knowledge Graph Builder.
"""

from pathlib import Path
from typing import Dict

from osef.core.ekg import KnowledgeGraph, Node, Edge
from osef.scanner.scanner import RepositoryScanner
from osef.parser.python import PythonParser
from osef.parser.symbol_table import SymbolTable
from osef.parser.resolvers.imports import ImportResolver
from osef.parser.resolvers.types import TypeResolver


class EKGBuilder:
    """
    Orchestrates the scanner and parser to build the Engineering Knowledge Graph.
    """

    def __init__(self, root_path: str | Path):
        self.root_path = Path(root_path).resolve()
        self.scanner = RepositoryScanner(self.root_path)
        self.symbol_table = SymbolTable()
        self.parser = PythonParser(self.symbol_table)
        self.graph = KnowledgeGraph()

    def build(self) -> KnowledgeGraph:
        """
        Scan, parse, and build the graph.
        """
        # 1. Scan and parse
        manifest = self.scanner.scan()
        for python_file in manifest.python_files:
            abs_path = self.root_path / python_file
            self.parser.parse_file(str(abs_path))

        # 2. Resolve Semantics
        import_resolver = ImportResolver(self.symbol_table)
        import_resolver.resolve()
        
        type_resolver = TypeResolver(self.symbol_table)
        type_resolver.resolve()

        # 3. Build Graph
        for symbol in self.symbol_table.symbols.values():
            node = Node(
                id=symbol.id,
                type=symbol.type,
                name=symbol.name,
                description=symbol.docstring,
                metadata={
                    "file_path": symbol.file_path,
                    "visibility": symbol.visibility,
                    **symbol.metadata
                }
            )
            self.graph.add_node(node)
            
        for symbol in self.symbol_table.symbols.values():
            # Edges for containment (parent -> child)
            for child_id in symbol.children_ids:
                edge = Edge(source_id=symbol.id, target_id=child_id, relation_type="CONTAINS")
                self.graph.add_edge(edge)
                
            # Specific edges for imports
            if symbol.type == "import" and symbol.metadata.get("resolved") == "true":
                target_id = symbol.metadata.get("resolved_to")
                if target_id:
                    edge = Edge(source_id=symbol.id, target_id=target_id, relation_type="IMPORTS")
                    self.graph.add_edge(edge)

        # 4. Validate
        if not self.graph.validate_graph():
            raise RuntimeError("Generated EKG is invalid (dangling edges).")

        return self.graph
