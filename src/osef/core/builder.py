"""
Engineering Knowledge Graph Builder.
"""

from pathlib import Path
import hashlib

from osef.core.ekg import KnowledgeGraph, Node, Edge
from osef.scanner.scanner import RepositoryScanner
from osef.parser.python import PythonParser
from osef.parser.models import ParsedModule


class EKGBuilder:
    """
    Orchestrates the scanner and parser to build the Engineering Knowledge Graph.
    """

    def __init__(self, root_path: str | Path):
        self.root_path = Path(root_path).resolve()
        self.scanner = RepositoryScanner(self.root_path)
        self.parser = PythonParser()
        self.graph = KnowledgeGraph()

    def _generate_id(self, *parts: str) -> str:
        """Generate a deterministic ID based on parts."""
        return hashlib.sha256(":".join(parts).encode("utf-8")).hexdigest()[:16]

    def build(self) -> KnowledgeGraph:
        """
        Scan, parse, and build the graph.
        """
        manifest = self.scanner.scan()

        for python_file in manifest.python_files:
            abs_path = self.root_path / python_file
            parsed_module = self.parser.parse_file(str(abs_path))
            self._incorporate_module(python_file, parsed_module)

        # Validate
        if not self.graph.validate_graph():
            raise RuntimeError("Generated EKG is invalid (dangling edges).")

        return self.graph

    def _incorporate_module(self, rel_path: str, parsed_module: ParsedModule) -> None:
        """Add nodes and edges for a parsed module."""
        module_id = self._generate_id("module", rel_path)
        
        module_node = Node(
            id=module_id,
            type="module",
            name=rel_path,
            description=parsed_module.docstring,
            metadata={"file_path": rel_path},
        )
        self.graph.add_node(module_node)

        # Add classes
        for cls in parsed_module.classes:
            cls_id = self._generate_id("class", rel_path, cls.name)
            cls_node = Node(
                id=cls_id,
                type="class",
                name=cls.name,
                description=cls.docstring,
                metadata={"bases": ",".join(cls.bases)},
            )
            self.graph.add_node(cls_node)
            self.graph.add_edge(Edge(source_id=module_id, target_id=cls_id, relation_type="CONTAINS"))

            # Add methods
            for method in cls.methods:
                method_id = self._generate_id("method", rel_path, cls.name, method.name)
                method_node = Node(
                    id=method_id,
                    type="method",
                    name=method.name,
                    description=method.docstring,
                    metadata={"is_async": str(method.is_async).lower()},
                )
                self.graph.add_node(method_node)
                self.graph.add_edge(Edge(source_id=cls_id, target_id=method_id, relation_type="CONTAINS"))

        # Add module-level functions
        for func in parsed_module.functions:
            func_id = self._generate_id("function", rel_path, func.name)
            func_node = Node(
                id=func_id,
                type="function",
                name=func.name,
                description=func.docstring,
                metadata={"is_async": str(func.is_async).lower()},
            )
            self.graph.add_node(func_node)
            self.graph.add_edge(Edge(source_id=module_id, target_id=func_id, relation_type="CONTAINS"))
