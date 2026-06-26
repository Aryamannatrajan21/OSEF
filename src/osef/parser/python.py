"""
Python AST Parser for the OSEF Framework.
"""

import ast
from typing import Any

from osef.parser.models import (
    ParsedModule,
    ParsedImport,
    ParsedClass,
    ParsedFunction,
    ParsedMethod,
    ParsedDecorator,
)


class PythonASTVisitor(ast.NodeVisitor):
    def __init__(self, file_path: str):
        self.module = ParsedModule(file_path=file_path)
        self._current_class: ParsedClass | None = None

    def visit_Module(self, node: ast.Module) -> Any:
        self.module.docstring = ast.get_docstring(node)
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> Any:
        for alias in node.names:
            self.module.imports.append(ParsedImport(module=alias.name))
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Any:
        if node.module:
            names = [alias.name for alias in node.names]
            self.module.imports.append(ParsedImport(module=node.module, names=names))
        self.generic_visit(node)

    def _parse_decorators(self, decorator_list: list[ast.expr]) -> list[ParsedDecorator]:
        decs = []
        for dec in decorator_list:
            if isinstance(dec, ast.Name):
                decs.append(ParsedDecorator(name=dec.id))
            elif isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name):
                decs.append(ParsedDecorator(name=dec.func.id))
            elif isinstance(dec, ast.Attribute):
                decs.append(ParsedDecorator(name=dec.attr))
        return decs

    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        bases = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                bases.append(base.id)
            elif isinstance(base, ast.Attribute):
                bases.append(base.attr)

        parsed_class = ParsedClass(
            name=node.name,
            bases=bases,
            docstring=ast.get_docstring(node),
            decorators=self._parse_decorators(node.decorator_list),
        )
        self.module.classes.append(parsed_class)

        # Visit methods
        prev_class = self._current_class
        self._current_class = parsed_class
        self.generic_visit(node)
        self._current_class = prev_class

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self._handle_function(node, is_async=False)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
        self._handle_function(node, is_async=True)

    def _handle_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef, is_async: bool) -> None:
        docstring = ast.get_docstring(node)
        decorators = self._parse_decorators(node.decorator_list)
        
        if self._current_class is not None:
            method = ParsedMethod(
                name=node.name,
                is_async=is_async,
                docstring=docstring,
                decorators=decorators,
            )
            self._current_class.methods.append(method)
        else:
            func = ParsedFunction(
                name=node.name,
                is_async=is_async,
                docstring=docstring,
                decorators=decorators,
            )
            self.module.functions.append(func)
            
        # Do not recursively visit function bodies to skip nested functions


class PythonParser:
    """
    Parses Python source code into OSEF Parser Models.
    """

    def parse_file(self, file_path: str) -> ParsedModule:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        return self.parse_source(source, file_path)

    def parse_source(self, source: str, file_path: str = "<string>") -> ParsedModule:
        tree = ast.parse(source, filename=file_path)
        visitor = PythonASTVisitor(file_path=file_path)
        visitor.visit(tree)
        return visitor.module
