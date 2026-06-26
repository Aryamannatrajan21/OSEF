"""
Models for the OSEF AST Parser.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class ParsedDecorator(BaseModel):
    name: str


class ParsedMethod(BaseModel):
    name: str
    is_async: bool
    docstring: Optional[str] = None
    decorators: List[ParsedDecorator] = Field(default_factory=list)


class ParsedClass(BaseModel):
    name: str
    bases: List[str] = Field(default_factory=list)
    docstring: Optional[str] = None
    methods: List[ParsedMethod] = Field(default_factory=list)
    decorators: List[ParsedDecorator] = Field(default_factory=list)


class ParsedFunction(BaseModel):
    name: str
    is_async: bool
    docstring: Optional[str] = None
    decorators: List[ParsedDecorator] = Field(default_factory=list)


class ParsedImport(BaseModel):
    module: str
    names: List[str] = Field(default_factory=list)


class ParsedModule(BaseModel):
    file_path: str
    docstring: Optional[str] = None
    imports: List[ParsedImport] = Field(default_factory=list)
    classes: List[ParsedClass] = Field(default_factory=list)
    functions: List[ParsedFunction] = Field(default_factory=list)
