# OSEF Version Transition History

This document tracks major version transitions and alignment with PEP 440.

```text
0.1.0
  ↓
0.2.0a0 (v0.2.0-alpha)
```

**Version Management Standard:**
- `pyproject.toml` is the single source of truth.
- `importlib.metadata.version("osef")` is used for dynamic resolution.
- Git tags match the public branding (e.g. `v0.2.0-alpha`).
- Python package versions strictly follow PEP 440 (e.g. `0.2.0a0`).
