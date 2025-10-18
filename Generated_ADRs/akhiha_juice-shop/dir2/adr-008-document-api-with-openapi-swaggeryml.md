---
### ADR-008: Document API with OpenAPI (swagger.yml)

Status: Inferred
Context: The repository contains swagger.yml alongside a large set of REST routes.
Decision: Maintain an OpenAPI specification for the service endpoints.
Consequences:
- Positive: Improves consumer understanding; enables tooling (clients, testing, documentation portals).
- Negative: Requires ongoing maintenance to avoid drift from implementation.