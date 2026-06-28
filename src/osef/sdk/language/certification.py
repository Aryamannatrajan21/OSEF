from typing import List, Dict
from pydantic import BaseModel, Field


class StageCertificationMetrics(BaseModel):
    passed: bool
    diagnostics: List[str] = Field(default_factory=list)
    execution_time_ms: float = 0.0


class CoverageMetrics(BaseModel):
    structural_coverage: float = 0.0
    inheritance_coverage: float = 0.0
    generics_coverage: float = 0.0
    decorators_coverage: float = 0.0
    imports_coverage: float = 0.0
    exports_coverage: float = 0.0
    visibility_coverage: float = 0.0
    call_graph_coverage: float = 0.0
    type_system_coverage: float = 0.0
    namespace_coverage: float = 0.0
    category_breakdown: Dict[str, float] = Field(default_factory=dict)


class PerformanceMetrics(BaseModel):
    parse_time_ms: float = 0.0
    symbol_extraction_time_ms: float = 0.0
    resolver_time_ms: float = 0.0
    semantic_time_ms: float = 0.0
    graph_mapping_time_ms: float = 0.0
    memory_usage_mb: float = 0.0
    throughput_nodes_per_sec: float = 0.0
    throughput_edges_per_sec: float = 0.0


class ParserCertificationReport(BaseModel):
    metrics: StageCertificationMetrics = Field(
        default_factory=StageCertificationMetrics
    )  # type: ignore


class SymbolCertificationReport(BaseModel):
    metrics: StageCertificationMetrics = Field(
        default_factory=StageCertificationMetrics
    )  # type: ignore
    stable_ids_verified: bool = False
    provenance_verified: bool = False


class ResolverCertificationReport(BaseModel):
    metrics: StageCertificationMetrics = Field(
        default_factory=StageCertificationMetrics
    )  # type: ignore


class StructuralSemanticReport(BaseModel):
    is_deterministic: bool
    fact_count: int


class DependencySemanticReport(BaseModel):
    is_deterministic: bool
    fact_count: int


class TypeSemanticReport(BaseModel):
    is_deterministic: bool
    fact_count: int


class VisibilitySemanticReport(BaseModel):
    is_deterministic: bool
    fact_count: int


class ExecutionSemanticReport(BaseModel):
    is_deterministic: bool
    fact_count: int


class SemanticCertificationReport(BaseModel):
    metrics: StageCertificationMetrics
    structural_report: StructuralSemanticReport
    dependency_report: DependencySemanticReport
    type_report: TypeSemanticReport
    visibility_report: VisibilitySemanticReport
    execution_report: ExecutionSemanticReport
    semantic_stability_verified: bool = False


class GraphCertificationReport(BaseModel):
    metrics: StageCertificationMetrics = Field(
        default_factory=StageCertificationMetrics
    )  # type: ignore
    graph_stability_verified: bool = False


class LanguageCertificationReport(BaseModel):
    """
    Canonical SDK artifact defining the certification status of a language processing pipeline.
    This replaces scattered markdown files with a highly structured, machine-readable validation object.
    """

    # Metadata
    language: str
    plugin_version: str
    sdk_version: str

    # Composable Certification Reports
    parser_report: ParserCertificationReport = Field(
        default_factory=ParserCertificationReport
    )
    symbol_report: SymbolCertificationReport = Field(
        default_factory=SymbolCertificationReport
    )
    resolver_report: ResolverCertificationReport = Field(
        default_factory=ResolverCertificationReport
    )
    semantic_report: SemanticCertificationReport = Field(
        default_factory=SemanticCertificationReport
    )  # type: ignore
    graph_report: GraphCertificationReport = Field(
        default_factory=GraphCertificationReport
    )

    # Determinism
    determinism_certification: StageCertificationMetrics = Field(
        default_factory=StageCertificationMetrics
    )  # type: ignore

    # Analytics
    coverage: CoverageMetrics = Field(default_factory=CoverageMetrics)
    performance: PerformanceMetrics = Field(default_factory=PerformanceMetrics)

    # Integration
    benchmarks: List[str] = Field(default_factory=list)

    # Final Outcome
    certification_decision: str = "PENDING"  # e.g., "PENDING", "FAILED", "CERTIFIED"
    recommendations: List[str] = Field(default_factory=list)
