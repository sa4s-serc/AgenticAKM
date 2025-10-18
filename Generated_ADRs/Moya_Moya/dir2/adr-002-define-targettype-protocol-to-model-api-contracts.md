---
### ADR-002: Define TargetType protocol to model API contracts

**Status:** Inferred
**Context:** Consistent modeling of endpoints is needed across different services while enabling testability and composability. Files like TargetType.swift and docs/Targets.md indicate a protocol-oriented approach for endpoint definition.
**Decision:** Introduce TargetType to describe an endpoint’s baseURL, path, method, headers, task, and sampleData.
**Consequences:** 
- Positive: Clear separation of API description from execution; strong typing; improves testability via sampleData.
- Negative: Learning curve for users; requires boilerplate per target definition.
- Trade-off: Protocol-oriented design prioritizes clarity and flexibility over minimal setup.