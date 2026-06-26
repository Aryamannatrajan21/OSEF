from osef.core.ekg import KnowledgeGraph
from osef.sdk.pipeline import PipelineContext
from osef.scanner.models import RepositoryManifest
from osef_documentation.enricher import DocumentationEnricher

def test_documentation_enricher(tmp_path):
    # Setup mock workspace
    doc1 = tmp_path / "README.md"
    doc2 = tmp_path / "docs" / "ARCHITECTURE.md"
    doc2.parent.mkdir()
    
    doc1.write_text("See [Architecture](docs/ARCHITECTURE.md)")
    doc2.write_text("Architecture details.")
    
    manifest = RepositoryManifest(name="test", version="1.0.0", root_path=str(tmp_path))
    from unittest.mock import MagicMock
    context = PipelineContext(
        workspace_dir=tmp_path,
        manifest=manifest,
        extension_context=MagicMock()
    )
    graph = KnowledgeGraph()
    
    enricher = DocumentationEnricher()
    delta = enricher.enrich(context, graph)
    
    assert len(delta.nodes_to_add) == 2
    
    node_ids = {n.id for n in delta.nodes_to_add}
    assert "doc:README.md" in node_ids
    assert "doc:docs/ARCHITECTURE.md" in node_ids
    
    assert len(delta.edges_to_add) == 1
    edge = delta.edges_to_add[0]
    assert edge.source_id == "doc:README.md"
    assert edge.target_id == "doc:docs/ARCHITECTURE.md"
    assert edge.relation_type == "REFERENCES"
