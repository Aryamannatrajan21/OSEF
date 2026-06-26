from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from osef.epe.core.severity import Severity
from osef.epe.core.category import Category


class Provenance(BaseModel):
    rule_id: str
    rule_version: str
    policy_version: str


class AutoFix(BaseModel):
    available: bool = False
    mutation_type: Optional[str] = None
    description: Optional[str] = None


class Evidence(BaseModel):
    description: str
    affected_nodes: List[str] = Field(default_factory=list)
    affected_edges: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Recommendation(BaseModel):
    action: str
    description: str


class Finding(BaseModel):
    id: str
    title: str
    description: str
    severity: Severity
    category: Category
    confidence: float
    provenance: Provenance
    evidence: Evidence
    recommendation: Recommendation
    autofix: AutoFix = Field(default_factory=AutoFix)
    documentation_links: List[str] = Field(default_factory=list)
    rfc_references: List[str] = Field(default_factory=list)
    adr_references: List[str] = Field(default_factory=list)


class RuleResult(BaseModel):
    findings: List[Finding] = Field(default_factory=list)
