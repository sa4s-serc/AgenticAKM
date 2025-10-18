---
### ADR-004: Centralize execution in MoyaProvider with configurable closures and stubbing

**Status:** Inferred
**Context:** Consumers need a single entry point for making requests, customizing behavior, and enabling deterministic testing. Files MoyaProvider.swift, MoyaProvider+Defaults.swift, MoyaProvider+Internal.swift and docs/Providers.md, docs/Testing.md support this.
**Decision:** Implement MoyaProvider to execute requests with injectable endpointClosure, requestClosure, and stubClosure, supporting immediate/delayed stubbing and dependency injection.
**Consequences:** 
- Positive: High configurability; testability through stubs; consistent execution pipeline.
- Negative: Additional abstraction may obscure underlying behavior; misconfiguration risk.
- Trade-off: Developer ergonomics and testing support over minimalism.