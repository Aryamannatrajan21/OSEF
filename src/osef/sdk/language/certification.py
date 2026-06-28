from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class StageCertificationMetrics(BaseModel):
    passed: bool
    diagnostics: List[str] = Field(default_factory=list)
    execution_time_ms: float = 0.0


class CoverageMetrics(BaseModel):
    total_symbols: int = 0
    resolved_symbols: int = 0
    coverage_percentage: float = 0.0
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


class LanguageCertificationReport(BaseModel):
    """
    Canonical SDK artifact defining the certification status of a language processing pipeline.
    This replaces scattered markdown files with a highly structured, machine-readable validation object.
    """
    # Metadata
    language: str
    plugin_version: str
    sdk_version: str
    
    # Certification Stages (Language Processing Certification)
    parser_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    symbol_extraction_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    resolver_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    semantic_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    graph_mapping_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    
    # Stability and Idempotence
    determinism_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    semantic_stability_certification: StageCertificationMetrics = Field(default_factory=StageCertificationMetrics)
    
    # Analytics
    coverage: CoverageMetrics = Field(default_factory=CoverageMetrics)
    performance: PerformanceMetrics = Field(default_factory=PerformanceMetrics)
    
    # Integration
    benchmarks: List[str] = Field(default_factory=list)
    
    # Final Outcome
    certification_decision: str = "PENDING"  # e.g., "PENDING", "FAILED", "CERTIFIED"
    recommendations: List[str] = Field(default_factory=list)
