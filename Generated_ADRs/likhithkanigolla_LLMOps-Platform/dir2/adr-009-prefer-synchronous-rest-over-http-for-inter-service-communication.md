---
### ADR-009: Prefer synchronous REST over HTTP for inter-service communication

Status: Inferred
Context: Widespread use of Flask for services and the requests library across requirements suggests RESTful HTTP for synchronous calls between services (e.g., controller, deployer, registries).
Decision: Implement inter-service synchronous communication using REST and the requests library; enable CORS where needed for browser-based frontend.
Consequences:
- Positive: Simplicity; broad tooling support; straightforward debugging.
- Negative: Tighter coupling and potential cascading failures under load; requires retries/circuit breakers for resilience.