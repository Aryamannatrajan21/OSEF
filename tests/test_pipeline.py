from osef.core.pipeline import PipelineEngine


def test_builder_creates_graph(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("""
class TestClass:
    def method(self):
        pass
def test_func():
    pass
""")

    builder = PipelineEngine(tmp_path)
    graph = builder.build()

    # module, class, method, function
    assert len(graph.nodes) == 4
    # module -> class, class -> method, module -> function
    assert len(graph.edges) == 3
