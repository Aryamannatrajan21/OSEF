from typing import Sequence
from copy import deepcopy
from osef.sdk.language.resolver import (
    LanguageResolver,
    ResolvedSymbolGraph,
    ResolvedRelationship,
)
from osef.sdk.language.symbols import NormalizedSymbol


class JavaResolver(LanguageResolver):
    """
    Immutable, pass-based resolver for Java.
    Consumes NormalizedSymbol objects and produces a ResolvedSymbolGraph
    with purely language-level relationships (e.g. IMPORTS, DECLARES, EXTENDS).
    """

    def resolve(self, symbols: Sequence[NormalizedSymbol]) -> ResolvedSymbolGraph:
        # Initialize an empty graph with nodes populated
        initial_graph = ResolvedSymbolGraph(nodes={s.symbol_id: s for s in symbols})

        # Execute deterministic passes, returning a new graph each time to ensure immutability
        g1 = self._pass_declarations(initial_graph)
        g2 = self._pass_imports_exports(g1)
        g3 = self._pass_inheritance(g2)

        return g3

    def _pass_declarations(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 1: Resolve namespace ownership declarations."""
        new_graph = deepcopy(graph)
        for symbol in new_graph.nodes.values():
            if symbol.kind in (
                "class",
                "interface",
                "enum",
            ):
                # symbol_id format is language::source_file::qualified_name::kind
                parts = symbol.symbol_id.split("::")
                if len(parts) >= 3:
                    qname = parts[2]
                    qname_parts = qname.split(".")
                    if len(qname_parts) > 1:
                        # It's inside a namespace (e.g. com.example)
                        namespace_name = ".".join(qname_parts[:-1])
                        for ns_symbol in new_graph.nodes.values():
                            ns_parts = ns_symbol.symbol_id.split("::")
                            if (
                                ns_symbol.kind == "namespace"
                                and len(ns_parts) >= 3
                                and ns_parts[2] == namespace_name
                            ):
                                new_graph.edges.append(
                                    ResolvedRelationship(
                                        relationship_id=f"{ns_symbol.symbol_id}_declares_{symbol.symbol_id}",
                                        source_symbol_id=ns_symbol.symbol_id,
                                        target_symbol_id=symbol.symbol_id,
                                        relationship_type="DECLARES",
                                    )
                                )
                                break
        return new_graph

    def _pass_imports_exports(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 2: Resolve cross-module import and export linkages."""
        new_graph = deepcopy(graph)
        for symbol in new_graph.nodes.values():
            if symbol.kind == "import":
                target_source = symbol.name
                if target_source:
                    new_graph.edges.append(
                        ResolvedRelationship(
                            relationship_id=f"{symbol.symbol_id}_imports_{target_source}",
                            source_symbol_id=symbol.symbol_id,
                            target_symbol_id=target_source,
                            relationship_type="DEPENDS_ON",
                        )
                    )
        return new_graph

    def _pass_inheritance(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 3: Resolve class/interface hierarchy."""
        new_graph = deepcopy(graph)
        for symbol in new_graph.nodes.values():
            if symbol.kind == "class" and "extends" in symbol.payload:
                parent_name = symbol.payload["extends"]
                for parent_symbol in new_graph.nodes.values():
                    if (
                        parent_symbol.kind == "class"
                        and parent_symbol.name == parent_name
                    ):
                        new_graph.edges.append(
                            ResolvedRelationship(
                                relationship_id=f"{symbol.symbol_id}_extends_{parent_symbol.symbol_id}",
                                source_symbol_id=symbol.symbol_id,
                                target_symbol_id=parent_symbol.symbol_id,
                                relationship_type="EXTENDS",
                            )
                        )
        return new_graph
