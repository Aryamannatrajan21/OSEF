from typing import Protocol, TypeVar, Generic, List, Sequence
from pydantic import BaseModel, Field

from .symbols import NormalizedSymbol
from .resolver import ResolvedSymbolGraph
from .facts import SemanticFact
from .certification import StageCertificationMetrics

T = TypeVar('T')

class Diagnostic(BaseModel):
    severity: str  # e.g., "ERROR", "WARNING", "INFO"
    stage: str
    symbol_id: str
    location: str
    message: str


class StageResult(BaseModel, Generic[T]):
    """
    Standardized return type for every stage in the language pipeline.
    Ensures that certification can proceed even if some symbols/files fail.
    """
    data: T
    diagnostics: List[Diagnostic] = Field(default_factory=list)
    metrics: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)


class LanguagePipeline(Protocol):
    """
    The canonical SDK Interface defining the universal language processing pipeline.
    Every language pack exposes the exact same execution surface.
    """
    
    def parse(self, source_file: str) -> StageResult:
        """Produces a NormalizedAST."""
        ...
        
    def extract_symbols(self, ast) -> StageResult[Sequence[NormalizedSymbol]]:
        """Produces a NormalizedSymbolModel from an AST."""
        ...
        
    def resolve(self, symbols: Sequence[NormalizedSymbol]) -> StageResult[ResolvedSymbolGraph]:
        """Produces a ResolvedSymbolGraph representing purely language relationships."""
        ...
        
    def analyze(self, graph: ResolvedSymbolGraph) -> StageResult[Sequence[SemanticFact]]:
        """Produces purely engineering knowledge as SemanticFacts."""
        ...
        
    def map_to_graph(self, facts: Sequence[SemanticFact]) -> StageResult:
        """Produces a GraphDelta to be merged into the Knowledge Graph."""
        ...
