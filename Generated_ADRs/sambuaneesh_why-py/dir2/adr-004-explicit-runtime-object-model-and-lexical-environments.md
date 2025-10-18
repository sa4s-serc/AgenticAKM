---
### ADR-004: Explicit Runtime Object Model and Lexical Environments

Status: Inferred
Context: object.py and environment.py indicate a dedicated type system for runtime values and a chained environment model for scoping and closures.
Decision: Represent runtime values (e.g., numbers, booleans, functions) via a custom object system and implement lexical scoping via chained Environment structures.
Consequences:
- Positive: Clear separation between syntax and semantics; easier to add types or built-ins; supports closures and nested scopes.
- Negative: Additional indirection and memory allocations; potential performance cost; requires careful handling of mutability and scope chains.