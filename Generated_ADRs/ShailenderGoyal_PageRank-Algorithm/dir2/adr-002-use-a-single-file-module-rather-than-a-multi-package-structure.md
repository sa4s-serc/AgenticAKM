---
### ADR-002: Use a single-file module rather than a multi-package structure

**Status:** Inferred
**Context:** Only one code file ("project.py") is present, with no package directories (e.g., no src/, no __init__.py files). This indicates a consolidated, single-module design.
**Decision:** Consolidate application logic into a single Python module (project.py).
**Consequences:** 
- Positive: Minimal setup, easy to read and run, low overhead for small scope.
- Negative: Reduced modularity and testability as the codebase grows; harder to reuse components; potential for a “god file” over time.