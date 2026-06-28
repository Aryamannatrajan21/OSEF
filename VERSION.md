# OSEF Version Transition History

This document tracks major version transitions and alignment with PEP 440.

```text
0.1.0
  ↓
1.0.0rc1 (v1.0.0-rc1)
  ↓
1.0.0 (v1.0.0 LTS)
```

**Version Management Standard:**
- `pyproject.toml` is the single source of truth.
- `importlib.metadata.version("osef")` is used for dynamic resolution.
- Git tags match the public branding (e.g. `v1.0.0-LTS`).
- Python package versions strictly follow PEP 440 (e.g. `1.0.0`).
