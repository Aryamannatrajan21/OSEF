from typing import Sequence

from osef.sdk.language.pipeline import LanguagePipeline
from osef.sdk.language.symbols import NormalizedSymbol
from osef.sdk.language.resolver import ResolvedSymbolGraph
from osef.sdk.language.facts import SemanticFact
from osef.sdk.language.builder import NormalizedSymbolBuilder

from .parser.adapter import TreeSitterJavaAdapter
from .extractor.extractor import JavaSymbolExtractor
from .resolver.resolver import JavaResolver
from .semantics.engine import JavaSemanticEngine
from .projections.mapper import GraphMapper, GraphDelta


class JavaPipeline(LanguagePipeline):
    """
    Standard orchestrator for Java.
    Executes parsing, extraction, resolution, semantics, and mapping.
    """

    def __init__(self):
        self.parser = TreeSitterJavaAdapter()
        self.builder = NormalizedSymbolBuilder(
            language="java",
            parser="tree-sitter",
            parser_version="0.23.5",
            sdk_version="0.1.0",
            plugin_version="1.0.0",
            graph_schema_version="5.0",
        )
        self.resolver = JavaResolver()
        self.semantics = JavaSemanticEngine()
        self.mapper = GraphMapper()

    def parse(self, source_file: str):
        return self.parser.parse(source_file)

    def extract_symbols(self, ast) -> Sequence[NormalizedSymbol]:
        # Generate a stable hash for the source file context
        # (in reality, we'd hash the file contents, but for now we mock it)
        source_hash = "mock_hash_for_java"

        extractor = JavaSymbolExtractor(self.builder, "test_file.java", source_hash)
        return extractor.extract(ast)

    def resolve(self, symbols: Sequence[NormalizedSymbol]) -> ResolvedSymbolGraph:
        return self.resolver.resolve(symbols)

    def analyze(self, graph: ResolvedSymbolGraph) -> Sequence[SemanticFact]:
        return self.semantics.analyze(graph)

    def map_to_graph(self, facts: Sequence[SemanticFact]) -> GraphDelta:
        return self.mapper.map_to_graph(facts)
