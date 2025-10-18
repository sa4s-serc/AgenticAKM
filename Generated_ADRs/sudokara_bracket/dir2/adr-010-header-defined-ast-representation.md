---
### ADR-010: Header-defined AST representation

Status: Inferred
Context: Only include/llracket/AST/AST.h is present; there is no corresponding AST.cpp, suggesting AST nodes and inline behavior are defined in headers.
Decision: Define AST node types and related inline utilities entirely in headers.
Consequences:
- Positive: Simplifies linkage; enables templated and inline utilities; reduces source fragmentation.
- Negative: Longer compile times on header changes; larger object files; tighter coupling through includes.