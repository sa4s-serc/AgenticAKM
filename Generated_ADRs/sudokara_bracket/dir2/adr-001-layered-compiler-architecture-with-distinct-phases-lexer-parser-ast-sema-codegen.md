### ADR-001: Layered compiler architecture with distinct phases (Lexer, Parser, AST, Sema, CodeGen)

Status: Inferred
Context: The repository is structured into modules under include/llracket and lib for Basic (diagnostics, tokens), Lexer, Parser, AST, Sema (semantic analysis), and CodeGen. This mirrors the traditional compiler pipeline and indicates an architectural need for clear separation of concerns, testability, and maintainability.
Decision: Implement the compiler as layered components: a Lexer producing tokens, a Parser building an AST, a Sema phase performing static checks, and a CodeGen phase emitting executable artifacts that rely on a small runtime.
Consequences: 
- Positive: Clear interfaces, easier unit testing, better maintainability, and the ability to evolve phases independently.
- Negative: More boilerplate and integration overhead; changes may ripple across module boundaries.