"""
Python AST Parser for the OSEF Framework.
"""

import ast
from typing import Any, Optional

from osef.parser.symbol_table import SymbolTable, Symbol, SourceLocation


class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self, symbol_table: SymbolTable, file_path: str):
        self.symbol_table = symbol_table
        self.file_path = file_path
        
        # We assume the module ID is derived from its file path
        self.module_id = self.symbol_table.generate_id("module", file_path)
        self._current_parent_id: Optional[str] = self.module_id

    def _create_location(self, node: ast.AST) -> SourceLocation:
        return SourceLocation(
            line=getattr(node, "lineno", 0),
            column=getattr(node, "col_offset", 0),
            end_line=getattr(node, "end_lineno", None),
            end_column=getattr(node, "end_col_offset", None),
        )

    def visit_Module(self, node: ast.Module) -> Any:
        module_symbol = Symbol(
            id=self.module_id,
            name=self.file_path.split("/")[-1] if "/" in self.file_path else self.file_path,
            type="module",
            file_path=self.file_path,
            docstring=ast.get_docstring(node),
        )
        self.symbol_table.add_symbol(module_symbol)
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> Any:
        for alias in node.names:
            import_id = self.symbol_table.generate_id("import", self.file_path, alias.name)
            import_sym = Symbol(
                id=import_id,
                name=alias.name,
                type="import",
                file_path=self.file_path,
                location=self._create_location(node),
                parent_id=self._current_parent_id,
                metadata={"asname": alias.asname or alias.name, "is_from": "false"}
            )
            self.symbol_table.add_symbol(import_sym)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        if node.module:
            for alias in node.names:
                import_id = self.symbol_table.generate_id("import", self.file_path, node.module, alias.name)
                import_sym = Symbol(
                    id=import_id,
                    name=alias.name,
                    type="import",
                    file_path=self.file_path,
                    location=self._create_location(node),
                    parent_id=self._current_parent_id,
                    metadata={"module": node.module, "asname": alias.asname or alias.name, "is_from": "true"}
                )
                self.symbol_table.add_symbol(import_sym)
        self.generic_visit(node)

    def _parse_decorators(self, decorator_list: list[ast.expr]) -> list[str]:
        decs = []
        for dec in decorator_list:
            if isinstance(dec, ast.Name):
                decs.append(dec.id)
            elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name):
                decs.append(dec.func.id)
            elif isinstance(dec, ast.Attribute):
                decs.append(dec.attr)
        return decs

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        bases = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                bases.append(base.id)
            elif isinstance(base, ast.Attribute):
                bases.append(base.attr)

        cls_id = self.symbol_table.generate_id("class", self.file_path, node.name)
        cls_sym = Symbol(
            id=cls_id,
            name=node.name,
            type="class",
            file_path=self.file_path,
            location=self._create_location(node),
            docstring=ast.get_docstring(node),
            parent_id=self._current_parent_id,
            metadata={
                "bases": ",".join(bases),
                "decorators": ",".join(self._parse_decorators(node.decorator_list)),
            }
        )
        self.symbol_table.add_symbol(cls_sym)

        # Visit methods
        prev_parent = self._current_parent_id
        self._current_parent_id = cls_id
        self.generic_visit(node)
        self._current_parent_id = prev_parent

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self._handle_function(node, is_async=False)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
        self._handle_function(node, is_async=True)

    def _handle_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef, is_async: bool) -> None:
        parent_sym = self.symbol_table.get_symbol(self._current_parent_id or "")
        func_type = "method" if parent_sym and parent_sym.type == "class" else "function"
        func_id = self.symbol_table.generate_id(func_type, self.file_path, str(self._current_parent_id), node.name)
        
        func_sym = Symbol(
            id=func_id,
            name=node.name,
            type=func_type,
            file_path=self.file_path,
            location=self._create_location(node),
            docstring=ast.get_docstring(node),
            parent_id=self._current_parent_id,
            metadata={
                "is_async": str(is_async).lower(),
                "decorators": ",".join(self._parse_decorators(node.decorator_list)),
            }
        )
        self.symbol_table.add_symbol(func_sym)
        # Do not recursively visit function bodies to skip nested functions


class PythonParser:
    """
    Parses Python source code into the OSEF Symbol Table.
    """
    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def parse_file(self, file_path: str) -> None:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        self.parse_source(source, file_path)

    def parse_source(self, source: str, file_path: str = "<string>") -> None:
        tree = ast.parse(source, filename=file_path)
        visitor = PythonASTVisitor(symbol_table=self.symbol_table, file_path=file_path)
        visitor.visit(tree)
