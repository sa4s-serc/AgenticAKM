---
### ADR-007: Perform static semantic analysis (type checking) in a dedicated Sema phase

Status: Inferred
Context: Presence of include/llracket/Sema and lib/Sema, and a tests/static_type suite with both .out and .err cases, indicates compile-time type checking and semantic validation.
Decision: Introduce a Sema module to perform static type checks and other semantic validations, emitting diagnostics for errors.
Consequences:
- Positive: Earlier error detection; clearer error messages; enables optimizations and safer code generation.
- Negative: Increased implementation effort; some dynamic patterns may be restricted; need to maintain type rules as language evolves.