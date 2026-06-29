from osef.core.pipeline import PipelineEngine

print("Starting")
try:
    engine = PipelineEngine(".")
    print("Engine created")
    graph = engine.build()
    print(f"Graph built with {len(graph.nodes)} nodes")
except Exception as e:
    print(f"Error: {e}")
