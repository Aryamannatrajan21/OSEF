from typing import Sequence
from copy import deepcopy
from osef.sdk.language.resolver import (
    LanguageResolver,
    ResolvedSymbolGraph,
    ResolvedRelationship,
)
from osef.sdk.language.symbols import NormalizedSymbol


class TypeScriptResolver(LanguageResolver):
    """
    Immutable, pass-based resolver for TypeScript.
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
        g4 = self._pass_type_resolution(g3)
        g5 = self._pass_call_resolution(g4)
        g6 = self._pass_reference_linking(g5)

        return g6

    def _pass_declarations(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 1: Resolve internal module and namespace ownership declarations."""
        new_graph = deepcopy(graph)
        # Find namespace ownership
        for symbol in new_graph.nodes.values():
            if symbol.kind in (
                "class",
                "interface",
                "function",
                "variable",
                "enum",
                "type_alias",
            ):
                parts = symbol.name.split(".")
                if len(parts) > 1:
                    # It's inside a namespace (e.g. MyNamespace.MyClass)
                    namespace_name = ".".join(parts[:-1])
                    # Try to find the namespace symbol in the graph
                    for ns_symbol in new_graph.nodes.values():
                        if (
                            ns_symbol.kind == "namespace"
                            and ns_symbol.name == namespace_name
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
                # Create a DEPENDS_ON edge for the import
                target_source = getattr(symbol, "source", None)
                if target_source:
                    new_graph.edges.append(
                        ResolvedRelationship(
                            relationship_id=f"{symbol.symbol_id}_imports_{target_source}",
                            source_symbol_id=symbol.symbol_id,
                            target_symbol_id=target_source,  # We leave it loose here for semantic engine to resolve against real files
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

    def _pass_type_resolution(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 4: Resolve generic bounds and type usages."""
        new_graph = deepcopy(graph)
        return new_graph

    def _pass_call_resolution(self, graph: ResolvedSymbolGraph) -> ResolvedSymbolGraph:
        """Pass 5: Resolve function/method invocations."""
        new_graph = deepcopy(graph)
        return new_graph

    def _pass_reference_linking(
        self, graph: ResolvedSymbolGraph
    ) -> ResolvedSymbolGraph:
        """Pass 6: Resolve general variable/symbol references."""
        new_graph = deepcopy(graph)
        return new_graph
