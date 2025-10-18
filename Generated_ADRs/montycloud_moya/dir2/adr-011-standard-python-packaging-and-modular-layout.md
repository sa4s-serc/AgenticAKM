---
### ADR-011: Standard Python Packaging and Modular Layout

Status: Inferred
Context: The library must be easy to install, distribute, and extend, with clear domain boundaries.
Decision: Use pyproject.toml for packaging and a modular directory structure aligned to domains (agents, orchestrators, memory, registry, tools, conversation).
Consequences:
- Positive: Adheres to modern Python packaging standards; clarity of module responsibilities; facilitates extension and testing.
- Negative: Cross-module dependencies must be managed carefully to avoid cyclical coupling.