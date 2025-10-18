---
### ADR-004: Implement a minimal runtime in C and link it with generated programs

Status: Inferred
Context: A runtime exists at tools/runtime/runtime.c/.h. Many tests involve I/O and data structures (e.g., vectors), which are typically supported by a small runtime the generated code can call into.
Decision: Build and ship a C runtime providing core primitives (e.g., I/O, data structure helpers) that the generated code relies on.
Consequences:
- Positive: Simplifies code generation; centralizes low-level operations; consistent behavior across programs.
- Negative: Additional artifact to build and link; C/C++ boundary management; runtime upgrades impact all generated programs.