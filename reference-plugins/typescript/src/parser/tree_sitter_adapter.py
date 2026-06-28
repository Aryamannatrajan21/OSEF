import tree_sitter_typescript as tsts
from tree_sitter import Language, Parser, Node
from .adapter import LanguageParserAdapter, NormalizedASTNode


class TreeSitterTypeScriptAdapter(LanguageParserAdapter):
    """
    Default parser adapter using Tree-sitter for TypeScript.
    """

    def __init__(self, is_tsx: bool = False):
        self.is_tsx = is_tsx
        lang = Language(tsts.language_tsx() if is_tsx else tsts.language_typescript())
        self.parser = Parser(lang)

    def parse(self, source_file: str) -> NormalizedASTNode:
        with open(source_file, "rb") as f:
            source_bytes = f.read()

        tree = self.parser.parse(source_bytes)
        return self._normalize_node(tree.root_node, source_bytes)

    def _normalize_node(self, node: Node, source_bytes: bytes) -> NormalizedASTNode:
        return NormalizedASTNode(
            kind=node.type,
            text=source_bytes[node.start_byte : node.end_byte].decode(
                "utf-8", errors="replace"
            ),
            start_line=node.start_point[0] + 1,  # 1-indexed for OSEF provenance
            start_column=node.start_point[1] + 1,
            end_line=node.end_point[0] + 1,
            end_column=node.end_point[1] + 1,
            children=[
                self._normalize_node(child, source_bytes) for child in node.children
            ],
        )

    def parser_name(self) -> str:
        return "tree-sitter-typescript"

    def parser_version(self) -> str:
        return tsts.__version__
