# OSEF Project-Scoped Agent Rules

These rules govern all agent behaviors, code implementations, and documentation workflows within the Open Source Engineering Framework (OSEF) repository.

## 1. Documentation & Markdown Invariants
- **No Raw HTML Iframes:** GitHub Markdown strips out `<iframe ...>`, `<script>`, and raw HTML embed tags for security reasons. When embedding interactive dashboards, launch videos, or external social media posts in markdown files (`README.md`, `COMMUNITY.md`, etc.), ALWAYS use clickable Markdown shields/badges or centered linked images:
  ```markdown
  [![Watch Video](https://img.shields.io/badge/LinkedIn-Watch_Video-0077b5?logo=linkedin)](https://target_url)
  ```
- **Preserve Unrelated Comments:** Maintain documentation integrity. Never delete or strip existing docstrings, comments, or architectural references unless explicitly instructed.
- **CLI Naming Symmetry:** Respect existing CLI conventions (`osef scan`, `osef report`, `osef ui`, `osef ecosystem`, `osef validate`, `osef certify`). Verify command flags against `README.md` before referencing them.

## 2. Tone & Communication Style
- **Zero AI-Speak:** Never use cliché marketing hyperbole (e.g., "thrilled," "beyond excited," "supercharge," "game-changer," "revolutionize"). 
- **Developer-to-Developer:** All commit messages, PR descriptions, documentation, and social copy must use a precise, professional, hacker-centric tone focused on technical mechanics and architectural facts.

## 3. Python Tooling, Git Discipline & CI/CD
- **Strict Linting Before Push:** The project enforces strict code formatting. Always run `ruff format .` and `ruff check .` locally before committing any Python changes.
- **Branch Verification:** Always check `git status` and `git branch` before committing to ensure changes are directed to the intended target branch (e.g., `main` vs. feature/release branches).
- **GitHub Actions Automation:** When designing automated workflows (like `publish-plugins.yml`), remember that automated PR creation requires explicit repository token permissions (`permissions: write-all` or "Allow GitHub Actions to create and approve pull requests").

## 4. Multi-Agent Delegation & Verification
- **Objective Verification Required:** When drafting task prompts or delegating work to subagents (including `/teamwork-preview`), every requirement must have an objective, programmatic verification mechanism (e.g., test scripts, SARIF schema validation, CLI exit codes).
- **No Self-Certification:** Implementing agents are strictly prohibited from evaluating or self-certifying their own subjective output. Always rely on verifiable test suites or independent auditor rubrics.

## 5. OSEF Architectural Positioning & Strategy
- **The Semantic Moat:** Always frame and design OSEF as an immutable, deterministic Engineering Knowledge Graph (EKG) and declarative Engineering Policy Engine (EPE).
- **Not an AST Linter or RAG:** Do not confuse or describe OSEF as a simple syntax checker (like ESLint/Ruff) or a naive LLM retrieval wrapper. All language adaptations must produce language-agnostic Symbol Tables and semantic facts.
- **Standardized Interchange over Custom Sync:** When implementing ecosystem integrations (Phase III), prioritize open industry standards (SARIF 2.1.0, JUnit XML, Model Context Protocol schemas) over building brittle, proprietary API integrations with third-party tools.
