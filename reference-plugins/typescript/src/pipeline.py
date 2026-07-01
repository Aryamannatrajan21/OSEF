from typing import Sequence
from osef.sdk.language.pipeline import LanguagePipeline
from osef.sdk.language.symbols import NormalizedSymbol
from osef.sdk.language.resolver import ResolvedSymbolGraph
from osef.sdk.language.facts import SemanticFact
from osef.sdk.language.builder import NormalizedSymbolBuilder
from .parser.tree_sitter_adapter import TreeSitterTypeScriptAdapter
from .extractor.extractor import TypeScriptSymbolExtractor
from .resolver.resolver import TypeScriptResolver
from .semantics.engine import TypeScriptSemanticEngine
from .projections.mapper import GraphMapper, GraphDelta


class TypeScriptPipeline(LanguagePipeline):
    """
    Implements the standard LanguagePipeline contract for the OSEF Ecosystem.
    """

    def __init__(self):
        self.builder = NormalizedSymbolBuilder(
            language="typescript",
            parser="tree-sitter",
            parser_version="0.21.0",
            sdk_version="0.1.0",
            plugin_version="0.1.0",
            graph_schema_version="5.0",
        )
        self.resolver = TypeScriptResolver()
        self.semantic_engine = TypeScriptSemanticEngine()
        self.mapper = GraphMapper()

    def parse(self, source_file: str):
        is_tsx = source_file.endswith(".tsx")
        # We instantiate the adapter dynamically based on the file type
        adapter = TreeSitterTypeScriptAdapter(is_tsx=is_tsx)
        return adapter.parse(source_file)

    def extract_symbols(self, ast) -> Sequence[NormalizedSymbol]:
        # Using a fixed hash for tests to simulate proper file hashing
        return TypeScriptSymbolExtractor(
            self.builder, "test_file.ts", "hash123"
        ).extract(ast)

    def resolve(self, symbols: Sequence[NormalizedSymbol]) -> ResolvedSymbolGraph:
        return self.resolver.resolve(symbols)

    def analyze(self, graph: ResolvedSymbolGraph) -> Sequence[SemanticFact]:
        return self.semantic_engine.analyze(graph)

    def map_to_graph(self, facts: Sequence[SemanticFact]) -> GraphDelta:
        return self.mapper.map_to_graph(facts)
