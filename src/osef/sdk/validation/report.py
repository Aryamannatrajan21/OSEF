"""
Platform Validation Report model.
"""

from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class ValidationTarget(BaseModel):
    type: str  # "Repository", "Workspace", "Fixture", "Plugin", "SDK", "Profile"
    identifier: str


class RepositoryMetadata(BaseModel):
    language: Optional[str] = None
    framework: Optional[str] = None
    repo_size: Optional[int] = None
    loc: Optional[int] = None
    packages: Optional[int] = None
    dependencies: Optional[int] = None
    commit: Optional[str] = None
    branch: Optional[str] = None
    analysis_date: Optional[str] = None


class GraphStatistics(BaseModel):
    node_count: int
    edge_count: int
    components: int
    services: int


class PlatformValidationReport(BaseModel):
    metadata: Dict[str, str] = Field(default_factory=dict)
    repository: Optional[RepositoryMetadata] = None
    profile: Optional[str] = None
    plugin_matrix: Dict[str, str] = Field(default_factory=dict)
    domain_coverage: List[str] = Field(default_factory=list)
    graph_statistics: Optional[GraphStatistics] = None
    correlation_statistics: Dict[str, int] = Field(default_factory=dict)
    reasoning_statistics: Dict[str, int] = Field(default_factory=dict)
    policy_statistics: Dict[str, int] = Field(default_factory=dict)
    certification: Dict[str, str] = Field(default_factory=dict)
    performance: Dict[str, float] = Field(default_factory=dict)
    sdk_compatibility: Dict[str, str] = Field(default_factory=dict)
    engineering_confidence: Dict[str, str] = Field(default_factory=dict)
    recommendations: List[str] = Field(default_factory=list)
