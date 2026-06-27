from pydantic import BaseModel, Field
from typing import List, Dict, Any


class EngineeringAssertion(BaseModel):
    """
    Universal regression language for Platform Certification.
    Defines an expected engineering state or policy finding.
    """

    id: str
    description: str
    expected_status: str = "FAIL"  # PASS, FAIL, WARNING
    evidence: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class GoldenSnapshot(BaseModel):
    """
    A golden engineering snapshot used for regression testing.
    Contains the expected state of the graph, correlations, reasoning, and policies.
    """

    version: str = "1.0.0"
    fixture_name: str
    nodes_count: int
    edges_count: int
    assertions: List[EngineeringAssertion] = Field(default_factory=list)
