"""
Platform Validation Report model.
"""

from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from osef.intelligence.models import EngineeringAssessment


class ValidationTarget(BaseModel):
    type: str  # "Repository", "Workspace", "Fixture", "Plugin", "SDK", "Profile"
    identifier: str


class GraphStatistics(BaseModel):
    node_count: int
    edge_count: int
    components: int
    services: int


class PlatformValidationReport(BaseModel):
    target: ValidationTarget
    profile: Optional[str] = None
    plugins_loaded: List[str] = Field(default_factory=list)
    graph_statistics: GraphStatistics
    ontology_validation: Dict[str, str] = Field(default_factory=dict)
    correlation_validation: Dict[str, str] = Field(default_factory=dict)
    reasoning_validation: Dict[str, str] = Field(default_factory=dict)
    policy_validation: Dict[str, str] = Field(default_factory=dict)
    certification_results: Dict[str, str] = Field(default_factory=dict)
    performance: Dict[str, float] = Field(default_factory=dict)
    sdk_gaps: List[str] = Field(default_factory=list)
    engineering_confidence: Dict[str, str] = Field(default_factory=dict)
    assessment: Optional[EngineeringAssessment] = None
