# OSEF AI IDE Integration Specification

## Overview
OSEF is the engineering knowledge layer for AI-assisted software development. It must integrate naturally with AI IDEs like Cursor, GitHub Copilot, Claude Code, OpenHands, and Aider.

The integration architecture must remain AI-provider agnostic.

## 1. Context Injection
AI IDEs lack standard engineering context. OSEF bridges this gap by generating `.osef/context.md` or `.cursorrules` files that inject the repository's architectural constraints directly into the LLM's system prompt.

Command:
```bash
osef export-context --target cursor
```
This generates a `.cursorrules` file containing the specific EKK rules relevant to the current repository profile.

## 2. Knowledge Loading
AI Agents can use the OSEF CLI as a tool. Instead of trying to guess Python standards, an agent like Claude Code can run:
```bash
osef rules search "python logging"
```
The CLI returns structured, machine-readable JSON (if requested) or Markdown that the agent reads to inform its code generation.

## 3. Continuous Review
As an AI Agent writes code, it can run `osef analyze` in a terminal sub-process to verify that its generated code adheres to the project's architectural constraints.

## 4. Prompt Composition
OSEF can act as a "Prompt Compiler." If a developer wants an AI to refactor a module, they can use OSEF to build a hyper-specific prompt that includes the EKK rules, the file contents, and the project's dependency graph.

## 5. Agnostic Architecture
OSEF does not hardcode integrations to specific LLM endpoints (unless via explicit optional plugins). Its primary integration mechanism is generating rich Markdown context files and providing a fast, deterministic CLI that any agentic framework can execute.
