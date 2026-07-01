import os
import re
from pathlib import Path
from typing import List
from osef.core.ekg import KnowledgeGraph, GraphDelta, Node, Edge
from osef.sdk.pipeline import PipelineContext


class DocumentationEnricher:
    """
    Discovers markdown documents, parses them, and produces a GraphDelta.
    """

    def __init__(self):
        # A simple regex for markdown links [text](url)
        self.link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def enrich(self, context: PipelineContext, graph: KnowledgeGraph) -> GraphDelta:
        delta = GraphDelta()

        doc_files = self._discover_docs(context.workspace_dir)

        for doc_path in doc_files:
            rel_path = doc_path.relative_to(context.workspace_dir)
            doc_id = f"doc:{rel_path}"

            # 1. Create Document Node
            node = Node(
                id=doc_id,
                type="document",
                name=doc_path.name,
                metadata={"file_path": str(rel_path), "layer": "documentation"},
            )
            delta.nodes_to_add.append(node)

            # 2. Parse Markdown for links
            links = self._parse_links(doc_path)
            for link_text, link_target in links:
                # Basic heuristic: if it's a local file link, create an edge
                if not link_target.startswith("http"):
                    # Resolve relative target
                    target_path = (doc_path.parent / link_target).resolve()
                    try:
                        target_rel = target_path.relative_to(context.workspace_dir)
                        target_id = f"doc:{target_rel}"
                        edge = Edge(
                            source_id=doc_id,
                            target_id=target_id,
                            relation_type="REFERENCES",
                            metadata={"text": link_text},
                        )
                        delta.edges_to_add.append(edge)
                    except ValueError:
                        # Outside workspace, ignore
                        pass

        return delta

    def _discover_docs(self, workspace_dir: Path) -> List[Path]:
        """Finds all markdown files, respecting basic ignores."""
        docs = []
        ignore_dirs = {".git", ".venv", "__pycache__", "node_modules", "build", "dist"}
        for root, dirs, files in os.walk(workspace_dir):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            for file in files:
                if file.endswith(".md"):
                    docs.append(Path(root) / file)
        return docs

    def _parse_links(self, doc_path: Path) -> List[tuple[str, str]]:
        """Extracts markdown links."""
        links = []
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
                matches = self.link_pattern.findall(content)
                for text, url in matches:
                    links.append((text, url))
        except Exception:
            pass
        return links
