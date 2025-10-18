### ADR-001: Adopt Python as the primary implementation language

**Status:** Inferred
**Context:** The repository contains Python source files (draw.py, extra.py) and no files indicating another runtime or language. This suggests the core logic is implemented in Python.
**Decision:** Implement the application in Python.
**Consequences:** 
- Positive: Rapid development, large standard library, broad ecosystem, ease of scripting and prototyping, cross-platform portability.
- Negative: Runtime dependency on a compatible Python interpreter, potential performance limitations compared to compiled languages, need to manage Python version compatibility.