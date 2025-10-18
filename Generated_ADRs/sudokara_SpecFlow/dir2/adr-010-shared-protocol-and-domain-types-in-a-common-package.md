---
### ADR-010: Shared protocol and domain types in a common package

Status: Inferred
Context: A common/ package contains protocol.py and __init__.py, intended for reuse by both edge and cloud components.
Decision: Centralize protocol messages, enums, and shared utilities in a common module to eliminate duplication and drift between client and server.
Consequences:
- Positive: Strong interoperability; single change point for protocol evolution; simplifies testing.
- Negative: Tight coupling on shared package version; requires careful backward compatibility management during updates.