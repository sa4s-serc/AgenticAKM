---
### ADR-009: Standardize error and response handling with MoyaError and Response

**Status:** Inferred
**Context:** Consumers need consistent error semantics and a uniform response type regardless of the underlying HTTP client. Files MoyaError.swift and Response.swift establish this.
**Decision:** Wrap outcomes in a Response type and propagate failures via MoyaError; provide built-in validation mechanisms (ValidationType).
**Consequences:** 
- Positive: Stable API; clearer error categorization; decouples consumers from Alamofire types.
- Negative: Potential information loss if mapping is imperfect; extra conversion steps.
- Trade-off: Consistency and decoupling over raw exposure of underlying errors.