from typing import List, Optional
from .symbols import (
    NormalizedSymbol,
    ParsingProvenance,
    SemanticProvenance,
    NormalizedClass,
    NormalizedInterface,
    NormalizedEnum,
    NormalizedTypeAlias,
    NormalizedFunction,
    NormalizedMethod,
    NormalizedProperty,
    NormalizedVariable,
    NormalizedNamespace,
    NormalizedModule,
    NormalizedImport,
    NormalizedExport,
    NormalizedGeneric,
    NormalizedDecorator,
    NormalizedConstructor,
    NormalizedConstant,
    NormalizedAnnotation,
    NormalizedTrait,
    NormalizedStruct
)


class StableSymbolIdGenerator:
    """Generates canonical stable IDs for symbols."""
    @staticmethod
    def generate(language: str, relative_path: str, qualified_name: str, symbol_kind: str) -> str:
        return f"{language}::{relative_path}::{qualified_name}::{symbol_kind}"


class NormalizedSymbolBuilder:
    """
    A generic builder used by Language-specific extractors to construct NormalizedSymbols.
    Ensures that standard fields and provenances are always correctly assembled.
    """
    def __init__(
        self,
        language: str,
        parser: str,
        parser_version: str,
        sdk_version: str,
        plugin_version: str,
        graph_schema_version: str
    ):
        self.language = language
        self.parser = parser
        self.parser_version = parser_version
        self.sdk_version = sdk_version
        self.plugin_version = plugin_version
        self.graph_schema_version = graph_schema_version

    def build(  # type: ignore
        self,
        symbol_class,
        source_file: str,
        source_hash: str,
        ast_node_kind: str,
        source_range: List[int],
        qualified_name: str,
        name: str,
        modifiers: Optional[List[str]] = None,
        type_hint: Optional[str] = None,
        docstring: Optional[str] = None,
        **kwargs
    ) -> NormalizedSymbol:
        kind = symbol_class.__fields__["kind"].default
        symbol_id = StableSymbolIdGenerator.generate(
            self.language, source_file, qualified_name, kind
        )
        
        parsing_prov = ParsingProvenance(
            language=self.language,
            parser=self.parser,
            parser_version=self.parser_version,
            source_file=source_file,
            source_hash=source_hash,
            ast_node_kind=ast_node_kind,
            source_range=source_range
        )
        
        semantic_prov = SemanticProvenance(
            semantic_stage="symbol_extraction",
            resolver_version="N/A",  # To be populated/updated in resolver
            plugin_version=self.plugin_version,
            sdk_version=self.sdk_version,
            graph_schema_version=self.graph_schema_version,
            normalized_symbol_id=symbol_id
        )
        
        return symbol_class(  # type: ignore
            symbol_id=symbol_id,
            name=name,
            parsing_provenance=parsing_prov,
            semantic_provenance=semantic_prov,
            modifiers=modifiers or [],
            type_hint=type_hint,
            docstring=docstring,
            **kwargs
        )
