from typing import Optional, List
from pydantic import BaseModel, Field


class ParsingProvenance(BaseModel):
    language: str
    parser: str
    parser_version: str
    source_file: str
    source_hash: str
    ast_node_kind: str
    source_range: List[int]  # [start_line, start_col, end_line, end_col]


class SemanticProvenance(BaseModel):
    semantic_stage: str
    resolver_version: str
    plugin_version: str
    sdk_version: str
    graph_schema_version: str
    normalized_symbol_id: str


class NormalizedSymbol(BaseModel):
    schema_version: str = "1.0"
    symbol_id: str
    name: str
    kind: str
    parsing_provenance: ParsingProvenance
    semantic_provenance: SemanticProvenance
    modifiers: List[str] = Field(default_factory=list)
    type_hint: Optional[str] = None
    docstring: Optional[str] = None
    payload: dict = Field(default_factory=dict)  # type: ignore


class NormalizedPackage(NormalizedSymbol):
    kind: str = "package"


class NormalizedModule(NormalizedSymbol):
    kind: str = "module"


class NormalizedNamespace(NormalizedSymbol):
    kind: str = "namespace"


class NormalizedImport(NormalizedSymbol):
    kind: str = "import"
    source: str  # The module/file being imported


class NormalizedExport(NormalizedSymbol):
    kind: str = "export"


class NormalizedClass(NormalizedSymbol):
    kind: str = "class"


class NormalizedInterface(NormalizedSymbol):
    kind: str = "interface"


class NormalizedTrait(NormalizedSymbol):
    kind: str = "trait"


class NormalizedStruct(NormalizedSymbol):
    kind: str = "struct"


class NormalizedEnum(NormalizedSymbol):
    kind: str = "enum"


class NormalizedTypeAlias(NormalizedSymbol):
    kind: str = "type_alias"


class NormalizedFunction(NormalizedSymbol):
    kind: str = "function"


class NormalizedMethod(NormalizedSymbol):
    kind: str = "method"


class NormalizedConstructor(NormalizedSymbol):
    kind: str = "constructor"


class NormalizedProperty(NormalizedSymbol):
    kind: str = "property"


class NormalizedVariable(NormalizedSymbol):
    kind: str = "variable"


class NormalizedConstant(NormalizedSymbol):
    kind: str = "constant"


class NormalizedGeneric(NormalizedSymbol):
    kind: str = "generic"


class NormalizedDecorator(NormalizedSymbol):
    kind: str = "decorator"


class NormalizedAnnotation(NormalizedSymbol):
    kind: str = "annotation"
