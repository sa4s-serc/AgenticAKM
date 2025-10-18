---
### ADR-009: Public headers under include/llracket with implementation in lib, following a library-style layout

Status: Inferred
Context: Headers are under include/llracket/* and sources under lib/*, mirroring an installable library structure and clean API/implementation separation.
Decision: Use an include/ (public API) and lib/ (implementation) split, with namespaced include paths (llracket/...) for clarity and potential installation.
Consequences:
- Positive: Clear boundaries; easier reuse; supports packaging and installation.
- Negative: Requires discipline to maintain API stability; potential duplication of declarations across headers.