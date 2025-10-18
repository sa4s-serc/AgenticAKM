---
### ADR-009: Single-target the backend and console to net7.0 (no multi-targeting)

Status: Inferred
Context: Both projects build only for net7.0 with no indications of multi-targeting in bin/obj outputs.
Decision: Build for a single target framework (net7.0) across all projects.
Consequences:
- Positive: Reduced build complexity and maintenance; consistent runtime behavior.
- Negative: Limits compatibility with other runtimes; porting to other targets later may require additional work.