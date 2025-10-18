---
### ADR-010: Minimal External Dependencies for the Interpreter

Status: Inferred
Context: The Python interpreter appears to rely on standard library modules only; dependencies are only present for the docs site.
Decision: Implement the interpreter in pure Python without third-party runtime dependencies.
Consequences:
- Positive: Easy setup; fewer security and compatibility concerns; portable across environments with Python installed.
- Negative: Re-implements capabilities that libraries might provide; potentially slower or less feature-rich than library-assisted approaches.