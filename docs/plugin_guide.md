# OSEF Plugin Development Guide

OSEF uses a modular plugin architecture to support multi-language parsing, custom rule packs, and architectural analyzers. This guide explains how to structure, build, sign, and publish a language plugin.

---

## 1. Plugin Structure

An OSEF plugin is a standard Python package containing a manifest (`plugin.yaml`) and an entry point implementing the OSEF parser or analyzer interface.

### Example Directory Layout
```text
reference-plugins/typescript/
├── plugin.yaml
├── pyproject.toml
├── src/
│   └── osef_ts/
│       ├── __init__.py
│       └── parser.py
```

---

## 2. Plugin Manifest (`plugin.yaml`)

The manifest defines metadata, capabilities, and compatibility constraints:
```yaml
id: osef-typescript
name: TypeScript Language Parser
version: 1.0.0
description: AST extractor and symbol table generator for TypeScript and JSX.
author: OSEF Core Team
license: MIT
capabilities:
  - language-parser
  - symbol-extraction
supported_languages:
  - typescript
  - javascript
entry_point: osef_ts.parser:TypeScriptParser
```

---

## 3. Implementing the Parser Interface

Plugins must subclass the abstract base parser or implement the standard symbol extraction contract:
```python
from typing import List, Dict, Any
from pathlib import Path

class TypeScriptParser:
    """Parses TypeScript source files into OSEF Symbol Tables."""
    
    def __init__(self, root_dir: Path) -> None:
        self.root_dir = root_dir

    def parse(self) -> List[Dict[str, Any]]:
        # Implement AST parsing logic (e.g. via tree-sitter or node CLI)
        symbols = []
        # Return standardized symbol definitions
        return symbols
```

---

## 4. Cryptographic Signing & Verification

To ensure chain-of-trust and prevent tampering, all plugins published to the OSEF Marketplace must be cryptographically signed using Ed25519 keys.

### Generate Keypair
```bash
osef plugin keygen --out ~/.osef/keys/
```

### Sign Plugin Archive
```bash
# Package plugin
tar -czf osef-typescript-1.0.0.tar.gz -C reference-plugins/typescript .

# Generate signature file (.sig)
osef plugin sign osef-typescript-1.0.0.tar.gz --key ~/.osef/keys/private.pem
```

### Verify Signature
```bash
osef plugin verify osef-typescript-1.0.0.tar.gz --sig osef-typescript-1.0.0.tar.gz.sig --pub ~/.osef/keys/public.pem
```

---

## 5. Publishing to Marketplace

To list your plugin in the root `marketplace-index.json`:
1. Submit a pull request adding your plugin metadata to `marketplace-index.json`.
2. Upon merging to `main`, the automated GitHub workflow (`publish-plugins.yml`) will verify signatures and publish release bundles.