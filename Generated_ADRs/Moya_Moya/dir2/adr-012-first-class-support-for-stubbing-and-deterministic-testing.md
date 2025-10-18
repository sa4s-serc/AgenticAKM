---
### ADR-012: First-class support for stubbing and deterministic testing

**Status:** Inferred
**Context:** Network-bound tests need determinism and speed. The repo has extensive tests, sampleData in TargetType, and docs/Testing.md explaining stubbing via MoyaProvider closures.
**Decision:** Make sampleData part of TargetType; offer stubbed providers with configurable response time and results; provide helpers for testing Combine/Rx/Reactive flows.
**Consequences:** 
- Positive: Fast, reliable tests; simpler integration testing; improved developer workflow.
- Negative: Risk of divergence from real server behavior; requires discipline to keep samples representative.
- Trade-off: Testability and speed over perfect fidelity to live services.