"""
Engineering Profile definition.
"""

from enum import Enum
from pydantic import BaseModel, Field
from typing import List


class CertificationLevel(str, Enum):
    BASIC = "basic"
    STANDARD = "standard"
    STRICT = "strict"
    ENTERPRISE = "enterprise"


class EngineeringProfile(BaseModel):
    name: str
    description: str
    inherits: List[str] = Field(default_factory=list)
    plugins: List[str] = Field(default_factory=list)
    policy_packs: List[str] = Field(default_factory=list)
    projections: List[str] = Field(default_factory=list)
    dashboards: List[str] = Field(default_factory=list)
    certification_levels: List[CertificationLevel] = Field(
        default_factory=lambda: [CertificationLevel.STANDARD]
    )
    capabilities: List[str] = Field(default_factory=list)
