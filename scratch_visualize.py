import sys
import os

# Add both core and visualization plugin to path
sys.path.insert(0, os.path.abspath("src"))
sys.path.insert(0, os.path.abspath("reference-plugins/visualization/src"))

from osef.core.ekg import KnowledgeGraph

# We'll construct a mock graph just to test the visualizer if we can't easily parse the whole repo here.
# But let's see if we can parse it.
try:

    # Actually the core parser is what we want.
    pass
except Exception:
    pass


def test_visualizer():
    # Build a tiny synthetic graph
    from osef.core.ekg import Node, Edge

    kg = KnowledgeGraph()
    kg.add_node(Node(id="pkg1", type="Package", name="osef"))
    kg.add_node(Node(id="mod1", type="Module", name="osef.core"))
    kg.add_node(Node(id="mod2", type="Module", name="osef.sdk"))
    kg.add_edge(Edge(source_id="pkg1", target_id="mod1", relation_type="contains"))
    kg.add_edge(Edge(source_id="pkg1", target_id="mod2", relation_type="contains"))
    kg.add_edge(Edge(source_id="mod1", target_id="mod2", relation_type="imports"))

    with open("test_ekg.json", "w") as f:
        f.write(kg.export_json())


if __name__ == "__main__":
    test_visualizer()
