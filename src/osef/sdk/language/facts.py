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


# ==========================================
# Structural Facts
# ==========================================

class ContainsFact(SemanticFact):
    fact_type: str = "contains"
    child_symbol_id: str


class NamespaceFact(SemanticFact):
    fact_type: str = "namespace"
    namespace_name: str


class ModuleFact(SemanticFact):
    fact_type: str = "module"
    module_name: str


# ==========================================
# Type System Facts
# ==========================================

class InheritanceFact(SemanticFact):
    fact_type: str = "inheritance"
    parent_symbol_id: str


class ImplementationFact(SemanticFact):
    fact_type: str = "implementation"
    interface_symbol_id: str


class GenericConstraintFact(SemanticFact):
    fact_type: str = "generic_constraint"
    constraint_symbol_id: str


class TypeAliasFact(SemanticFact):
    fact_type: str = "type_alias"
    aliased_symbol_id: str


class TypeUsageFact(SemanticFact):
    fact_type: str = "type_usage"
    type_symbol_id: str


# ==========================================
# Dependencies Facts
# ==========================================

class ImportFact(SemanticFact):
    fact_type: str = "import"
    imported_symbol_id: str


class ExportFact(SemanticFact):
    fact_type: str = "export"
    exported_symbol_id: str


class DependencyFact(SemanticFact):
    fact_type: str = "dependency"
    dependency_symbol_id: str


# ==========================================
# Execution Facts
# ==========================================

class CallFact(SemanticFact):
    fact_type: str = "call"
    target_symbol_id: str


class OverrideFact(SemanticFact):
    fact_type: str = "override"
    overridden_symbol_id: str


class VisibilityFact(SemanticFact):
    fact_type: str = "visibility"
    level: str  # public, private, protected, package


# ==========================================
# Ownership & Metadata Facts
# ==========================================

class OwnershipFact(SemanticFact):
    fact_type: str = "ownership"
    owned_symbol_id: str


class DocumentationFact(SemanticFact):
    fact_type: str = "documentation"
    docstring: str


class AnnotationFact(SemanticFact):
    fact_type: str = "annotation"
    annotation_symbol_id: str


class DecoratorFact(SemanticFact):
    fact_type: str = "decorator"
    decorator_symbol_id: str
