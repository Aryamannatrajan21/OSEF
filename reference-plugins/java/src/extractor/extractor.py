from typing import List, Sequence, Optional
from osef.sdk.language.symbols import (
    NormalizedSymbol,
    NormalizedClass,
    NormalizedInterface,
    NormalizedEnum,
    NormalizedNamespace,
)
from osef.sdk.language.builder import NormalizedSymbolBuilder
from src.parser.adapter import NormalizedASTNode


class JavaSymbolExtractor:
    """
    Translates a parser-specific NormalizedAST into the parser-independent NormalizedSymbolModel.
    Extraction is strictly limited to identifying symbols; it does NOT resolve relationships.
    """

    def __init__(
        self, builder: NormalizedSymbolBuilder, source_file: str, source_hash: str
    ):
        self.builder = builder
        self.source_file = source_file
        self.source_hash = source_hash

    def extract(self, ast: NormalizedASTNode) -> Sequence[NormalizedSymbol]:
        symbols: List[NormalizedSymbol] = []

        # In Java, the package is declared at the file level
        file_namespace = ""
        for child in ast.children:
            if child.kind == "package_declaration":
                name = self._extract_package_name(child)
                if name:
                    file_namespace = name
                    symbols.append(
                        self._build_symbol(
                            NormalizedNamespace, child, file_namespace, name
                        )
                    )
                    break

        self._walk(ast, symbols, file_namespace)
        return symbols

    def _walk(
        self,
        node: NormalizedASTNode,
        symbols: List[NormalizedSymbol],
        namespace: str,
    ):
        if node.kind == "class_declaration":
            name = self._find_child_text(node, "identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(self._build_symbol(NormalizedClass, node, qname, name))

        elif node.kind == "interface_declaration":
            name = self._find_child_text(node, "identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(
                    self._build_symbol(NormalizedInterface, node, qname, name)
                )

        elif node.kind == "enum_declaration":
            name = self._find_child_text(node, "identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(self._build_symbol(NormalizedEnum, node, qname, name))

        for child in node.children:
            self._walk(child, symbols, namespace)

    def _extract_package_name(self, node: NormalizedASTNode) -> Optional[str]:
        # A package declaration might contain a scoped_identifier (com.example) or identifier (com)
        for child in node.children:
            if child.kind in ("scoped_identifier", "identifier"):
                return child.text
        return None

    def _find_child_text(self, node: NormalizedASTNode, kind: str) -> Optional[str]:
        for child in node.children:
            if child.kind == kind:
                return child.text
        return None

    def _build_symbol(
        self, symbol_class, node: NormalizedASTNode, qualified_name: str, name: str
    ) -> NormalizedSymbol:
        return self.builder.build(
            symbol_class=symbol_class,
            source_file=self.source_file,
            source_hash=self.source_hash,
            ast_node_kind=node.kind,
            source_range=[
                node.start_line,
                node.start_column,
                node.end_line,
                node.end_column,
            ],
            name=name,
            qualified_name=qualified_name,
            modifiers=[],
        )
