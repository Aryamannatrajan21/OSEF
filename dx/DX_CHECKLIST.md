# OSEF Developer Experience Checklist

Before any PR is merged, new CLI command is added, or Plugin is published, it MUST pass this Developer Experience evaluation matrix.

## 1. Discoverability
- [ ] Is the command clearly listed in the `--help` menu?
- [ ] Does the `--help` output provide at least two realistic examples?
- [ ] Are aliases (if any) intuitive?

## 2. Consistency
- [ ] Does the command follow the `verb noun` structure (e.g., `osef analyze repo`, not `osef repo-analyze`)?
- [ ] Do flags follow standard POSIX conventions (e.g., `--force`, `--dry-run`)?
- [ ] Are colors used consistently (Red = Error, Yellow = Warning, Green = Success, Blue = Info)?

## 3. Cognitive Load
- [ ] Can the command be run without passing any configuration arguments? (Does it have sane defaults?)
- [ ] Does the command complete successfully on a standard repository without requiring a 10-page manual?
- [ ] Are complex configuration options hidden behind progressive disclosure (e.g., `--advanced`)?

## 4. Engineering Quality
- [ ] Does this command improve the repository's health, rather than just generating a file?
- [ ] Does it cite its reasoning using the EKK?

## 5. Architectural Integrity
- [ ] Does this feature rely on public Service Contracts, ensuring plugin compatibility?
- [ ] Would an experienced Python developer consider the SDK implementation intuitive and Pythonic?

## 6. Error Handling
- [ ] If the command fails, does the error message explain *What happened*, *Why*, and *How to fix it*?
- [ ] Does the error avoid raw stack traces unless `--verbose` or `--debug` is passed?

## 7. Contributor Empathy
- [ ] Can a new contributor understand what this feature does by reading its docstring?
- [ ] Is the feature documented in a User Story?
