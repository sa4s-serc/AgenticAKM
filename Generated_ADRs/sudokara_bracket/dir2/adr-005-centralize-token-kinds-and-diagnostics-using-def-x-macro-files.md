---
### ADR-005: Centralize token kinds and diagnostics using .def (X-macro) files

Status: Inferred
Context: include/llracket/Basic/TokenKinds.def and Diagnostic.def are paired with TokenKinds.cpp and Diagnostic.cpp. This pattern is commonly used to keep enums, string tables, and metadata in sync.
Decision: Use .def files to define tokens and diagnostics once, generating strongly-typed enums and related tables across components.
Consequences:
- Positive: Single source of truth; consistency across Lexer/Parser/Diagnostics; easier to extend.
- Negative: X-macro pattern can be unfamiliar; macro misuse can be hard to debug; IDEs may not navigate generated constructs well.