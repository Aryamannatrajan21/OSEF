import tree_sitter
import tree_sitter_java
from typing import List
from pydantic import BaseModel, Field
import hashlib


class ParsingProvenance(BaseModel):
    source_file: str
    source_hash: str
    parser: str = "tree-sitter-java"
    parser_version: str = "0.23.5"
    language: str = "java"


class NormalizedASTNode(BaseModel):
    kind: str
    text: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    provenance: ParsingProvenance
    children: List["NormalizedASTNode"] = Field(default_factory=list)


class TreeSitterJavaAdapter:
    def __init__(self):
        self.language = tree_sitter.Language(tree_sitter_java.language())
        self.parser = tree_sitter.Parser()
        self.parser.language = self.language

    def parse(self, source_file: str) -> NormalizedASTNode:
        with open(source_file, "rb") as f:
            source_bytes = f.read()

        source_hash = hashlib.sha256(source_bytes).hexdigest()
        tree = self.parser.parse(source_bytes)

        provenance = ParsingProvenance(source_file=source_file, source_hash=source_hash)

        return self._convert_node(tree.root_node, source_bytes, provenance)

    def _convert_node(
        self, node, source_bytes: bytes, provenance: ParsingProvenance
    ) -> NormalizedASTNode:
        kind = node.type

        children = []
        for child in node.children:
            if child.is_named:
                children.append(self._convert_node(child, source_bytes, provenance))

        text = source_bytes[node.start_byte : node.end_byte].decode("utf8")

        return NormalizedASTNode(
            kind=kind,
            text=text,
            start_line=node.start_point[0] + 1,
            start_column=node.start_point[1] + 1,
            end_line=node.end_point[0] + 1,
            end_column=node.end_point[1] + 1,
            provenance=provenance,
            children=children,
        )

    def parser_name(self) -> str:
        return "tree-sitter-java"

    def parser_version(self) -> str:
        return "0.23.5"
