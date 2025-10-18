---
### ADR-011: Introduce MultiTarget to unify multiple target enums under one provider

**Status:** Inferred
**Context:** Apps often call multiple APIs with distinct TargetType enums but want to use a single provider instance. The presence of MultiTarget.swift and related tests confirms this pattern.
**Decision:** Provide a MultiTarget wrapper that erases the concrete TargetType, enabling heterogeneous requests through one MoyaProvider.
**Consequences:** 
- Positive: Simplifies provider management; reduces boilerplate when integrating multiple services.
- Negative: Loss of some compile-time type specificity and enum exhaustiveness.
- Trade-off: Convenience and flexibility vs. strict type guarantees.