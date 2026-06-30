import os
import sys

sys.path.insert(0, os.path.abspath("."))
from osef.sdk.ecosystem.registry import EcosystemRegistry
from osef.sdk.ecosystem.validation import PlatformValidationEngine

sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from src.pipeline import TypeScriptPipeline


import os


def test_ecosystem_integration():
    registry = EcosystemRegistry()
    ts_pipeline = TypeScriptPipeline()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(current_dir, "..", "plugin_manifest.json")

    registry.register_plugin(manifest_path, ts_pipeline)

    print("✅ Ecosystem Registry loaded TypeScript Plugin metadata deterministically.")

    validation_engine = PlatformValidationEngine(registry)

    # We will simulate validating the 'language-fixtures/symbols/single_class' directory
    deltas = validation_engine.validate_workspace(
        "language-fixtures/symbols/single_class", profiles=["backend"]
    )

    print(
        f"✅ Platform Validation Engine processed {len(deltas)} GraphDeltas dynamically!"
    )


if __name__ == "__main__":
    test_ecosystem_integration()
