# OSEF CLI Reference

The `osef` command-line interface is built on Typer and provides deterministic commands for building Symbol Tables, evaluating constitutional engineering policies, launching local servers, and integrating with standard ecosystem pipelines.

## Global Options

```bash
osef [COMMAND] [OPTIONS]
```

* `--help`: Display usage documentation for the command.

---

## Core Engine Commands

### `osef scan`

Scans a target project directory using language-specific parser plugins (Python, TypeScript, Java) to construct the deterministic Engineering Knowledge Graph (EKG) and write artifact bundles to disk.

```bash
osef scan [TARGET_DIR] [OPTIONS]
```

**Options**:
* `--output`, `-o`: Directory to store generated EKG JSON and graph bundles (default: `.osef/`).
* `--format`: Output serialization format (`json`, `yaml`, `sarif`).

**Example**:
```bash
osef scan /path/to/project --format json --output .osef/
```

### `osef validate`

Executes end-to-end EKG graph integrity validation, topological sorting, and structural constraint verification against the target project.

```bash
osef validate repository [TARGET_DIR] [OPTIONS]
```

**Example**:
```bash
osef validate repository .
```

### `osef report`

Generates markdown or HTML architecture assessment summaries and engineering intelligence metrics.

```bash
osef report [TARGET_DIR] [OPTIONS]
```

---

## Policy Engine (EPE) Commands

### `osef policy check`

Evaluates declarative architectural policies against the EKG and outputs standardized violation reports.

```bash
osef policy check [TARGET_DIR] [OPTIONS]
```

**Options**:
* `--format`: Report output format: `table` (default), `sarif` (SARIF 2.1.0), or `junit` (JUnit XML).
* `--output`, `-o`: File path to write the formatted report (e.g., `results.sarif`).
* `--ci`: CI/CD mode. Exits with non-zero exit code (`1`) if any `CRITICAL` or `HIGH` severity findings are encountered.

**Examples**:
```bash
# Run local check with rich table output
osef policy check .

# CI/CD SARIF export for GitHub Advanced Security / CodeQL
osef policy check . --format sarif --output osef-policy-results.sarif --ci

# JUnit XML export for Jenkins / GitLab CI
osef policy check . --format junit --output junit-results.xml --ci
```

---

## Ecosystem & Marketplace Commands

### `osef benchmark publish`

Runs the OSEF Intelligence Layer to compute engineering confidence, technical debt, and architecture drift scores, generating a static web leaderboard bundle.

```bash
osef benchmark publish [OPTIONS]
```

**Options**:
* `--target`, `-t`: Target repository path to analyze (default: `.`).
* `--output`, `-o`: Directory to output static leaderboard bundle (default: `benchmark-site`).

### `osef marketplace build`

Validates reference plugin manifests (`plugin.yaml`) and cryptographic signatures, building a standalone static HTML/JSON marketplace bundle.

```bash
osef marketplace build [OPTIONS]
```

**Options**:
* `--out-dir`, `-o`: Output directory for generated static marketplace (default: `marketplace-site`).
* `--index-path`, `-i`: Path to root plugin marketplace index (default: `marketplace-index.json`).

### `osef plugin`

Manages cryptographic keys, plugin package signing, verification, installation, and searching.

```bash
osef plugin [SUBCOMMAND] [OPTIONS]
```

**Subcommands**:
* `search <query>`: Search the marketplace index for language plugins.
* `install <plugin_id>`: Install and verify a plugin from the marketplace index.
* `keygen`: Generate an Ed25519 keypair for signing plugin archives.
* `sign <archive_path>`: Sign a tarball using an Ed25519 private key.
* `verify <archive_path>`: Verify archive signature against public key.

---

## Universal Distribution & Integration Commands

### `osef mcp serve`

Starts a Model Context Protocol (MCP) server over standard input/output (`stdio`), exposing EKG query tools and architectural assessment resources directly to LLM clients (VS Code, Antigravity IDE, Claude Desktop).

```bash
osef mcp serve [TARGET_DIR]
```

**Exposed MCP Tools**:
* `blast_radius`: Calculate dependents and dependencies for a symbol or file.
* `dependency_path`: Find shortest structural dependency path between two symbols.
* `policy_violations`: List architectural policy violations filtered by category.
* `architecture_summary`: Retrieve high-level project architectural assessment metrics.
* `symbol_info`: Lookup AST symbol definition details and references.

### `osef ui`

Launches the local OSEF Studio development server or opens the dashboard interface.

```bash
osef ui [OPTIONS]
```

### `osef doctor`

Diagnoses environment readiness, installed language parsers, and system dependencies.

```bash
osef doctor
```