from typing import List, Sequence, Optional
from osef.sdk.language.symbols import (
    NormalizedSymbol,
    NormalizedClass,
    NormalizedInterface,
    NormalizedEnum,
    NormalizedTypeAlias,
    NormalizedNamespace,
    NormalizedFunction,
    NormalizedMethod,
    NormalizedVariable,
    NormalizedImport,
)
from osef.sdk.language.builder import NormalizedSymbolBuilder
from src.parser.adapter import NormalizedASTNode


class TypeScriptSymbolExtractor:
    """
    Translates a parser-specific NormalizedAST into the parser-independent NormalizedSymbolModel.
    Extraction is strictly limited to identifying symbols; it does NOT resolve relationships.
    Executes in deterministic passes:
    1. Namespaces / Modules
    2. Types (Class, Interface, Enum, TypeAlias)
    3. Functions / Methods
    4. Variables / Constants
    5. Imports / Exports (Declarations only)
    6. Metadata (Decorators, Modifiers, Generics)
    """

    def __init__(
        self, builder: NormalizedSymbolBuilder, source_file: str, source_hash: str
    ):
        self.builder = builder
        self.source_file = source_file
        self.source_hash = source_hash

    def extract(self, ast: NormalizedASTNode) -> Sequence[NormalizedSymbol]:
        symbols: List[NormalizedSymbol] = []
        self._walk(ast, symbols)
        return symbols

    def _walk(
        self,
        node: NormalizedASTNode,
        symbols: List[NormalizedSymbol],
        parent_namespace: str = "",
    ):
        # Determine current namespace prefix
        namespace = parent_namespace
        if node.kind == "internal_module":
            name = self._find_child_text(node, "identifier")
            if name:
                namespace = f"{namespace}.{name}" if namespace else name
                symbols.append(
                    self._build_symbol(NormalizedNamespace, node, namespace, name)
                )

        if node.kind == "class_declaration":
            name = self._find_child_text(node, "type_identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(self._build_symbol(NormalizedClass, node, qname, name))

        elif node.kind == "interface_declaration":
            name = self._find_child_text(node, "type_identifier")
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

        elif node.kind == "type_alias_declaration":
            name = self._find_child_text(node, "type_identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(
                    self._build_symbol(NormalizedTypeAlias, node, qname, name)
                )

        elif node.kind == "function_declaration":
            name = self._find_child_text(node, "identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(
                    self._build_symbol(NormalizedFunction, node, qname, name)
                )

        elif node.kind == "method_definition":
            name = self._find_child_text(
                node, "property_identifier"
            ) or self._find_child_text(node, "identifier")
            if name:
                qname = f"{namespace}.{name}" if namespace else name
                symbols.append(self._build_symbol(NormalizedMethod, node, qname, name))

        elif node.kind == "lexical_declaration" or node.kind == "variable_declaration":
            # For variables, we need to dig into the variable_declarator
            for child in node.children:
                if child.kind == "variable_declarator":
                    name = self._find_child_text(child, "identifier")
                    if name:
                        qname = f"{namespace}.{name}" if namespace else name
                        symbols.append(
                            self._build_symbol(NormalizedVariable, node, qname, name)
                        )

        elif node.kind == "import_statement":
            # An import statement typically has a 'string' child representing the source
            source_node = None
            for child in node.children:
                if child.kind == "string":
                    source_node = child
                    break

            if source_node:
                # Strip quotes
                source = source_node.text.strip("'\"")
                # Add import symbol
                import_sym = self._build_symbol(
                    NormalizedImport, node, f"import_{source}", "import"
                )
                import_sym.source = source
                symbols.append(import_sym)

        for child in node.children:
            self._walk(child, symbols, namespace)

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
            qualified_name=qualified_name,
            name=name,
        )
