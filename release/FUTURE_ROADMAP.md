# OSEF Future Roadmap

## Overview
This roadmap outlines the strategic direction for OSEF beyond the `v1.0.0` local-first MVP.

## Version 1.x (Post-MVP Growth)
*Focus: Ecosystem stabilization and Language expansion.*
- **Multi-Language Support:** Expand OSTE beyond Python ASTs to support TypeScript, Rust, and Go.
- **Advanced GitHub Integration:** Official GitHub App for automated PR reviews based on EKK rules.
- **IDE Extensions:** Official VS Code and JetBrains plugins providing real-time architectural feedback, eliminating the need for context-export workarounds.

## Version 2.x (The Knowledge Era)
*Focus: Advanced querying and Semantic understanding.*
- **Graph Database Backend:** Transition internal rule linking from SQLite/Memory to a true Graph schema (e.g., NetworkX or Neo4j).
- **Vector Search Plugin:** Official integration with local embedding models to allow natural language queries against the codebase architecture.
- **Plugin Marketplace:** Launch the official registry for third-party OSEF plugins.

## Version 3.x (Enterprise & Cloud)
*Focus: Team collaboration and Distributed analysis.*
- **Team Workspaces:** Allow teams to share custom EKK rulesets across an organization privately.
- **Distributed Runtime:** Enable OSEF to run headless across distributed compute nodes for massive monorepos.
- **Enterprise Governance Dashboard:** Web-based UI tracking Open Source certification scores across a company's entire repository portfolio.

## Research & Experimental
- **Multi-Agent Runtime:** Evolving OSEF from an "Engineering OS" to an "Agentic Runtime," where autonomous agents can register with the Event Bus, request context, and propose architectural refactoring PRs autonomously.
