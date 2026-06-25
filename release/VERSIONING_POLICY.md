# OSEF Versioning Policy

## 1. Semantic Versioning
OSEF strictly adheres to [SemVer 2.0.0](https://semver.org/).
Given a version number `MAJOR.MINOR.PATCH`:
- **MAJOR:** Incompatible API changes.
- **MINOR:** Backward compatible functionality additions.
- **PATCH:** Backward compatible bug fixes.

## 2. Pre-Release Designations
- **Alpha (`1.0.0-alpha.x`):** Core functionality exists but is highly unstable. Public API is NOT guaranteed.
- **Beta (`1.0.0-beta.x`):** Feature complete. Public API is considered stable but may change if critical flaws are found. 
- **Release Candidate (`1.0.0-rc.x`):** Believed to be production-ready. No new features accepted. Only critical bug fixes.

## 3. Backward Compatibility Scope
The backward compatibility guarantee applies **strictly** to:
1. `osef.contracts` (The Protocols).
2. `osef.core.context` (The Domain Models).
3. `osef.init()` (The SDK Bootstrapper).
4. CLI argument signatures.
5. The structure of the Markdown EKK parsing rules.

## 4. Plugin Compatibility
Plugins depend on the `osef.contracts`. Because Contracts are guaranteed across MINOR versions, a plugin written for `v1.0.0` MUST work without modification on `v1.9.9`. 
If a Plugin imports from `osef.services` (internal API), it forfeits this guarantee.

## 5. Deprecation Strategy
- A feature slated for removal must be marked as `@deprecated` in code and documentation for at least one full MINOR version lifecycle.
- The CLI must emit a `DeprecationWarning` if the feature is used.
