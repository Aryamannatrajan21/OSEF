from typing import Any, Dict
from pydantic import BaseModel, Field


class SemanticFact(BaseModel):
    """
    Language-independent engineering facts extracted by a Semantic Engine.
    These are consumed by the GraphMapper to produce GraphDeltas.
    """
    subject_symbol_id: str
    fact_type: str
    attributes: Dict[str, Any] = Field(default_factory=dict)


class InheritanceFact(SemanticFact):
    fact_type: str = "inheritance"
    parent_symbol_id: str


class ImplementationFact(SemanticFact):
    fact_type: str = "implementation"
    interface_symbol_id: str


class ImportFact(SemanticFact):
    fact_type: str = "import"
    imported_symbol_id: str


class CallFact(SemanticFact):
    fact_type: str = "call"
    target_symbol_id: str


class OwnershipFact(SemanticFact):
    fact_type: str = "ownership"
    owned_symbol_id: str


class VisibilityFact(SemanticFact):
    fact_type: str = "visibility"
    level: str  # public, private, protected, package


class TypeUsageFact(SemanticFact):
    fact_type: str = "type_usage"
    type_symbol_id: str
