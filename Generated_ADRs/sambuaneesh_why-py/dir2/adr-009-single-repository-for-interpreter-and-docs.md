---
### ADR-009: Single Repository for Interpreter and Docs

Status: Inferred
Context: Python interpreter and Node-based documentation are co-located; the docs package is private and uses local copy steps.
Decision: Maintain a monorepo containing both the interpreter and the documentation site.
Consequences:
- Positive: Simplifies cross-references; single source of truth; coordinated versioning and CI; easier contributor onboarding.
- Negative: Mixed tooling (Python and Node) complicates environment setup; larger repository footprint; potential coupling of release cycles.