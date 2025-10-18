---
### ADR-002: Use a flat, script-oriented project structure (non-packaged)

**Status:** Inferred
**Context:** Python files are located at the repository root with no package directories or __init__.py, and there is no setup.py/pyproject.toml to define a distributable package.
**Decision:** Organize code as top-level scripts/modules rather than a formal Python package.
**Consequences:** 
- Positive: Simplicity, low overhead to run or modify scripts, minimal onboarding friction.
- Negative: Harder to scale and organize as codebase grows, more difficult imports and reuse, packaging and distribution via PyPI are not straightforward, test discovery and tooling integration can be limited.