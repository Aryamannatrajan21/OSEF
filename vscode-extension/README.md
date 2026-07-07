# OSEF VS Code Extension & Studio Workbench

The official Visual Studio Code integration for the Open Source Engineering Framework (OSEF).

## Features

- **Interactive EKG Visualization**: Embeds OSEF Studio directly inside VS Code webviews (`osef.startStudio`).
- **One-Click Repository Validation**: Run declarative symbol table and graph validation (`osef.validateRepo`).
- **Policy Enforcement & SARIF Reporting**: Evaluate architectural policies and view findings in VS Code output channels (`osef.policyCheck`).
- **Engineering Status Explorer**: Dedicated sidebar view (`osef-status-view`) monitoring EKG state, Marketplace index, and MCP server readiness.

## Usage

1. Start the OSEF Studio UI server in your terminal:
   ```bash
   osef ui
   ```
2. Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run `OSEF: Open Studio Workbench`.
3. Check the OSEF Studio sidebar icon on the activity bar for real-time graph and policy metrics.
