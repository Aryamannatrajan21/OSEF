"""
Organizational Knowledge Model (OKM).
"""

from pydantic import BaseModel
from typing import Optional


class OrganizationalTeam(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


class OrganizationalMember(BaseModel):
    id: str
    username: str
    email: Optional[str] = None


class OrganizationalRole(BaseModel):
    id: str
    name: str


class OrganizationalBusinessUnit(BaseModel):
    id: str
    name: str


class OrganizationalProduct(BaseModel):
    id: str
    name: str


class OrganizationalServiceCatalog(BaseModel):
    id: str
    name: str
