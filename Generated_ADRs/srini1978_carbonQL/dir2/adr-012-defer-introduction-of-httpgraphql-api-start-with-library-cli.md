---
### ADR-012: Defer introduction of HTTP/GraphQL API; start with library + CLI

Status: Inferred
Context: Despite the project name hinting at query-like functionality, there are no web-hosting, REST, or GraphQL packages; only a library and console are present.
Decision: Postpone building a networked API surface and focus first on core computation in a library, invoked via a CLI host.
Consequences:
- Positive: Faster iteration on core logic; avoids premature infrastructure complexity.
- Negative: No remote access or integration endpoints; adding an API later will require additional hosting, routing, and contract design.