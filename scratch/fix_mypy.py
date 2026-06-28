import os
import re

def replace_in_file(filepath, replacements):
    with open(filepath, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w') as f:
        f.write(content)

# Fix src/osef/sdk/language/symbols.py
replace_in_file('src/osef/sdk/language/symbols.py', [
    ('class NormalizedObject(NormalizedSymbol):', 'class NormalizedObject(NormalizedSymbol):\n    properties: dict[str, Any] = {}'),
    ('metadata: dict = Field(default_factory=dict)', 'metadata: dict[str, Any] = Field(default_factory=dict)')
])

# Fix src/osef/sdk/language/certification.py
replace_in_file('src/osef/sdk/language/certification.py', [
    ('default_factory=StageCertificationMetrics', 'default_factory=lambda: StageCertificationMetrics()'),
    ('default_factory=SemanticCertificationReport', 'default_factory=lambda: SemanticCertificationReport()')
])

# Fix src/osef/sdk/language/pipeline.py
replace_in_file('src/osef/sdk/language/pipeline.py', [
    ('default_factory=StageCertificationMetrics', 'default_factory=lambda: StageCertificationMetrics()'),
    ('StageResult:', 'StageResult[Any]:'),
    ('-> StageResult', '-> StageResult[Any]'),
    ('def __init__(self, parser, builder)', 'def __init__(self, parser: Any, builder: Any) -> None:')
])

# Fix src/osef/sdk/plugin.py
replace_in_file('src/osef/sdk/plugin.py', [
    ('license: str | None = None\n    homepage: str | None = None\n    repository: str | None = None\n    documentation: str | None = None\n    keywords: list[str] = Field(default_factory=list)', '')
])

# Fix src/osef/sdk/registry/ecosystem.py
replace_in_file('src/osef/sdk/registry/ecosystem.py', [
    ('manifest_data = yaml.safe_load(f)', 'manifest_data: dict[str, Any] = yaml.safe_load(f)'),
    ('def discover(self)', 'def discover(self) -> None:')
])

# Fix src/osef/sdk/ecosystem/registry.py
replace_in_file('src/osef/sdk/ecosystem/registry.py', [
    ('def register_plugin(self, manifest)', 'def register_plugin(self, manifest: Any) -> None:'),
    ('def register_language_pipeline(self, pipeline)', 'def register_language_pipeline(self, pipeline: Any) -> None:'),
    ('self.plugins: dict = {}', 'self.plugins: dict[str, Any] = {}'),
    ('self.language_pipelines: dict = {}', 'self.language_pipelines: dict[str, Any] = {}')
])

# Fix src/osef/sdk/ecosystem/validation.py
replace_in_file('src/osef/sdk/ecosystem/validation.py', [
    ('def validate_all(self, profiles=None)', 'def validate_all(self, profiles: list[str] | None = None) -> Any:')
])

# Fix src/osef/cli/main.py
replace_in_file('src/osef/cli/main.py', [
    ('stats.node_count', 'getattr(stats, "node_count", 0)'),
    ('stats.edge_count', 'getattr(stats, "edge_count", 0)')
])

print("Fixes applied.")
