import os
import tempfile
import pytest

from src.pipeline import JavaPipeline


@pytest.fixture
def java_pipeline():
    return JavaPipeline()


def test_java_pipeline_end_to_end(java_pipeline):
    source_code = """
    package com.example;

    public class MyClass extends ParentClass {
        public void myMethod() {
        }
    }
    
    interface MyInterface {
    }
    """

    with tempfile.NamedTemporaryFile(suffix=".java", delete=False, mode="w") as f:
        f.write(source_code)
        temp_file = f.name

    try:
        # Parse
        ast = java_pipeline.parse(temp_file)
        assert ast is not None

        # Extract Symbols
        symbols = java_pipeline.extract_symbols(ast)
        assert len(symbols) == 4  # Namespace, Class, Interface, Method

        class_symbol = next(s for s in symbols if s.kind == "class")
        assert class_symbol.name == "MyClass"

        # Resolve
        graph = java_pipeline.resolve(symbols)
        # Should have a DECLARES edge from namespace to class and interface
        assert len(graph.edges) == 2

        # Analyze
        facts = java_pipeline.analyze(graph)
        assert len(facts) > 0

        # Map
        delta = java_pipeline.map_to_graph(facts)
        assert len(delta.nodes) > 0
    finally:
        os.remove(temp_file)
