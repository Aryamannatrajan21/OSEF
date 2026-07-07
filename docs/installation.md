# OSEF Installation & Universal Distribution Guide

OSEF is designed as a portable, universal engineering policy and analysis framework. You can run OSEF locally via Python virtual environments, containerize it using Docker OCI images, or integrate it into IDEs and CI/CD pipelines.

---

## 1. Local Python Installation (pip / venv)

OSEF requires **Python 3.12+**. It is recommended to install within an isolated virtual environment.

### Clone and Install in Editable Mode
```bash
git clone https://github.com/Aryamannatrajan21/OSEF.git
cd OSEF

# Create and activate virtual environment
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install core framework with development and documentation dependencies
pip install --upgrade pip
pip install -e ".[dev,docs,ui]"

# Verify installation
osef doctor
osef --help
```

---

## 2. Docker Containerization (OCI Image)

OSEF provides a multi-stage, hardened Dockerfile for reproducible execution in any container runtime (Docker, Podman, Kubernetes).

### Build the Image
```bash
docker build -t osef:latest .
```

### Run Commands Inside Container
Mount your project directory to `/workspace` inside the container:
```bash
# Scan and validate local project
docker run --rm -v $(pwd):/workspace osef:latest validate repository .

# Run EPE policy check and generate SARIF report
docker run --rm -v $(pwd):/workspace osef:latest policy check . --format sarif --output results.sarif
```

---

## 3. VS Code / Antigravity IDE Extension (VSIX Sideloading)

The official OSEF IDE extension provides real-time policy evaluation, MCP server integration, and architecture graph visualization.

### Installing from CLI
```bash
code --install-extension vscode-extension/osef-vscode-0.1.1.vsix
```
*(For Cursor or Windsurf, substitute `code` with `cursor` or `windsurf`)*.

### Installing from IDE GUI
1. Open the **Extensions** panel (`Ctrl+Shift+X` or `Cmd+Shift+X`).
2. Click the `...` (More Actions) menu in the top right corner.
3. Select **Install from VSIX...**.
4. Browse to `vscode-extension/osef-vscode-0.1.1.vsix` and install.

---

## 4. GitHub Actions CI/CD Integration

You can integrate OSEF policy evaluation directly into pull request workflows using the root composite action (`action.yml`).

### Example `.github/workflows/osef-policy-check.yml`
```yaml
name: OSEF Policy Check
on: [pull_request, push]

permissions:
  contents: read
  security-events: write

jobs:
  policy-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run OSEF Policy Evaluation
        uses: ./
        with:
          target: '.'
          format: 'sarif'
          output: 'osef-policy-results.sarif'
          ci: 'true'

      - name: Upload SARIF to GitHub Code Scanning
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: osef-policy-results.sarif
          category: osef-epe
```