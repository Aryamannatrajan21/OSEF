import pytest
from osef.core.ekg import Node, Edge, KnowledgeGraph, EKGError


def test_ekg_node_creation():
    node = Node(id="1", type="document", name="Vision")
    assert node.id == "1"
    assert node.type == "document"


def test_ekg_edge_validation():
    kg = KnowledgeGraph()
    n1 = Node(id="A", type="doc", name="A")
    n2 = Node(id="B", type="doc", name="B")

    kg.add_node(n1)
    kg.add_node(n2)

    edge = Edge(source_id="A", target_id="B", relation_type="DEPENDS_ON")
    kg.add_edge(edge)

    assert kg.validate_graph() is True


def test_ekg_invalid_edge():
    kg = KnowledgeGraph()
    n1 = Node(id="A", type="doc", name="A")
    kg.add_node(n1)

    edge = Edge(source_id="A", target_id="MISSING", relation_type="DEPENDS_ON")
    with pytest.raises(EKGError):
        kg.add_edge(edge)
