"""
Models for the Repository Scanner.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class RepositoryManifest(BaseModel):
    """
    A manifest representing the discovered files and project metadata.
    """

    root_path: str
    project_name: Optional[str] = None
    python_files: List[str] = Field(default_factory=list)
    typescript_files: List[str] = Field(default_factory=list)
    java_files: List[str] = Field(default_factory=list)
    has_pyproject: bool = False
    has_requirements: bool = False
    package_manager: Optional[str] = None
