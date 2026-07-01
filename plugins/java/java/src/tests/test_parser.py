import pytest
import os
import hashlib
import json
import sys

sys.path.append(os.path.abspath("reference-plugins/java"))
from src.parser.adapter import TreeSitterJavaAdapter, NormalizedASTNode

import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.parent.parent.parent
FIXTURE_PATH = str(
    PROJECT_ROOT
    / "language-fixtures"
    / "parser"
    / "java"
    / "single_class"
    / "source.java"
)
SNAPSHOT_PATH = str(
    PROJECT_ROOT
    / "language-fixtures"
    / "parser"
    / "java"
    / "single_class"
    / "snapshot.json"
)


@pytest.fixture
def parser():
    return TreeSitterJavaAdapter()


def test_determinism(parser):
    """Execute parsing 100 consecutive times. All serialized AST hashes must be identical."""
    hashes = set()
    for _ in range(100):
        ast = parser.parse(FIXTURE_PATH)
        ast_json = ast.model_dump_json()
        h = hashlib.sha256(ast_json.encode()).hexdigest()
        hashes.add(h)

    assert len(hashes) == 1, (
        "Determinism failed! Multiple hashes produced across 100 runs."
    )


def test_snapshot_integrity(parser):
    """Generate deterministic JSON snapshots. Verify byte-for-byte equality."""
    ast = parser.parse(FIXTURE_PATH)
    ast_json = ast.model_dump_json(indent=2)

    snapshot_path = SNAPSHOT_PATH

    if not os.path.exists(snapshot_path):
        with open(snapshot_path, "w") as f:
            f.write(ast_json)

    with open(snapshot_path, "r") as f:
        snapshot = f.read()

    assert ast_json == snapshot, "Snapshot integrity failed!"


def test_provenance(parser):
    """Every AST node must contain complete parsing provenance."""
    ast = parser.parse(FIXTURE_PATH)

    def check_node(node: NormalizedASTNode):
        assert node.provenance.source_file == FIXTURE_PATH
        assert node.provenance.language == "java"
        assert len(node.provenance.source_hash) == 64
        assert node.start_line > 0
        assert node.start_column > 0

        for child in node.children:
            check_node(child)

    check_node(ast)


def test_serialization(parser):
    """AST -> JSON -> Deserialize -> AST must be bit-for-bit identical."""
    ast = parser.parse(FIXTURE_PATH)
    ast_json = ast.model_dump_json()

    ast_reloaded = NormalizedASTNode.model_validate_json(ast_json)
    ast_reloaded_json = ast_reloaded.model_dump_json()

    assert ast_json == ast_reloaded_json, "Serialization equivalence failed!"


def test_hash_stability(parser, tmp_path):
    """Formatting changes (whitespace) must not change canonical structural identity, but full AST captures it."""
    # Note: Full AST serialization *will* change with whitespace.
    # But for "Hash Stability", if we remove text and provenance, the structure must remain identical.
    ast_original = parser.parse(FIXTURE_PATH)

    whitespace_source = tmp_path / "source.java"
    whitespace_source.write_text(
        '\n\n\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}\n'
    )
    ast_whitespace = parser.parse(str(whitespace_source))

    def structural_hash(node: NormalizedASTNode) -> str:
        """Hash the structure independent of location and text."""
        struct = {
            "kind": node.kind,
            "children": [structural_hash(c) for c in node.children],
        }
        return hashlib.sha256(json.dumps(struct, sort_keys=True).encode()).hexdigest()

    assert structural_hash(ast_original) == structural_hash(ast_whitespace), (
        "Structural Hash Stability failed!"
    )
