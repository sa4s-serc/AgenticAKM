### ADR-001: Choose Python as the implementation language

**Status:** Inferred
**Context:** The repository contains a single source file named "project.py" and no files from other language ecosystems. This strongly indicates the codebase is implemented in Python.
**Decision:** Implement the project in Python.
**Consequences:** 
- Positive: Broad platform support, fast iteration, rich standard library, and ease of onboarding for Python users.
- Negative: Potential performance limitations compared to compiled languages; dependency on a compatible Python runtime; packaging/distribution considerations differ from compiled binaries.