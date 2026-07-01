"""
Compliance Knowledge Model.
"""

from pydantic import BaseModel
from typing import Optional


class ComplianceRequirement(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


class ComplianceFramework(BaseModel):
    id: str
    name: str


class ComplianceControl(BaseModel):
    id: str
    name: str


class ComplianceEvidence(BaseModel):
    id: str
    name: str


class ComplianceException(BaseModel):
    id: str
    reason: str


class CompliancePolicy(BaseModel):
    id: str
    name: str
