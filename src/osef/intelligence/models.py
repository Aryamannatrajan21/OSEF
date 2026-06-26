"""
Domain models for Engineering Intelligence.
"""

from typing import List
from pydantic import BaseModel, Field


class ArchitectureAssessment(BaseModel):
    services: int
    controllers: int
    repositories: int
    dtos: int
    exceptions: int
    total_components: int


class DependencyAssessment(BaseModel):
    total_imports: int
    resolved_imports: int
    broken_imports: int
    external_dependencies: List[str]


class DocumentationAssessment(BaseModel):
    total_elements: int
    documented_elements: int
    undocumented_elements: int
    coverage_percentage: float


class EngineeringAssessment(BaseModel):
    architecture: ArchitectureAssessment
    dependencies: DependencyAssessment
    documentation: DocumentationAssessment
    findings: List[str] = Field(default_factory=list)
