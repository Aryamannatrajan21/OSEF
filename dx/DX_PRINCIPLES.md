# OSEF Developer Experience Principles

Every interaction within OSEF must be intentionally designed to reinforce the following principles.

## 1. Discoverability
A developer should never hit a dead end. Every CLI output, API response, and error message must answer: "What can I do next?" Commands should feature rich `--help` menus with realistic examples.

## 2. Predictability
Same inputs yield same outputs. OSEF must not rely on hidden state. The side effects of a command (e.g., mutating a repository) must be explicitly requested or confirmed.

## 3. Consistency
Command taxonomy (`verb noun`), configuration precedence, and SDK method signatures must adhere strictly to established patterns across the entire Core and all Plugins.

## 4. Transparency
OSEF does not do "magic". If it modifies `pyproject.toml`, it prints a diff or a clear log stating *why* it modified it, tracing the decision back to an EKK rule.

## 5. Low Cognitive Load
Developers come to OSEF to save time, not to learn another complex system. Sane defaults must be provided for everything. Configuration is optional.

## 6. Explicit over Implicit
If a plugin alters Core behavior, the CLI must explicitly state that the plugin is active and responsible for the behavior.

## 7. Knowledge before Prompts
Before prompting a user for input, OSEF should attempt to infer the answer from the repository context (via the EKK). If it asks a question, it should provide a recommended answer based on engineering standards.

## 8. Plugins before Monoliths
Features that are not universally applicable (e.g., Java-specific linting, Kubernetes deployments) must exist as Plugins, keeping the Core UX clean and fast.

## 9. Helpful Error Messages
Errors must teach. See the [Error Recovery Guidelines](ERROR_RECOVERY_GUIDELINES.md).

## 10. Progressive Disclosure
Advanced flags (`--verbose`, `--dry-run`, `--audit-level`) are hidden from standard outputs until the user explicitly asks for deeper complexity.

## 11. Offline First
Core initialization, EKK queries, and local repository audits must function on an airplane.

## 12. Community First
Plugins, themes, and EKK rules must be easy to author, share, and install, empowering the community to drive the ecosystem.
