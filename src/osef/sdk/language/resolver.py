from typing import List, Dict, Protocol, Sequence, Any
from pydantic import BaseModel, Field
from .symbols import NormalizedSymbol


class ResolvedRelationship(BaseModel):
    """A canonical language-level relationship between two symbols."""
    relationship_id: str
    source_symbol_id: str
    target_symbol_id: str
    relationship_type: str  # DECLARES, IMPORTS, EXPORTS, EXTENDS, IMPLEMENTS, CALLS, USES_TYPE, RETURNS, REFERENCES, CONTAINS, OVERRIDES
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ResolverDiagnostics(BaseModel):
    """Metadata regarding the resolution pass."""
    unresolved_imports: List[str] = Field(default_factory=list)
    duplicate_symbols: List[str] = Field(default_factory=list)
    circular_references: List[str] = Field(default_factory=list)
    missing_declarations: List[str] = Field(default_factory=list)
    unsupported_syntax: List[str] = Field(default_factory=list)
    resolution_confidence: float = 1.0


class ResolvedSymbolGraph(BaseModel):
    """An immutable container representing a resolved language graph."""
    nodes: Dict[str, NormalizedSymbol] = Field(default_factory=dict)
    edges: List[ResolvedRelationship] = Field(default_factory=list)
    diagnostics: ResolverDiagnostics = Field(default_factory=ResolverDiagnostics)


class LanguageResolver(Protocol):
    """
    Protocol defining the contract for any language resolver.
    The resolver must consume a sequence of NormalizedSymbols and produce
    an immutable ResolvedSymbolGraph via deterministic, semantic passes.
    """
    def resolve(self, symbols: Sequence[NormalizedSymbol]) -> ResolvedSymbolGraph:
        ...
