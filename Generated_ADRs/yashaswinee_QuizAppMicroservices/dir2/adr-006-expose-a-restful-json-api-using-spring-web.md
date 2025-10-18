---
### ADR-006: Expose a RESTful JSON API using Spring Web

Status: Inferred
Context: The system must provide HTTP endpoints for question and quiz operations consumable by clients (e.g., web/mobile).
Decision: Use spring-boot-starter-web and annotate controllers to serve RESTful JSON endpoints.
Consequences:
- Positive: Standard, widely supported approach; integrates easily with clients and API tooling.
- Negative: Requires careful design for error handling, input validation, and versioning (not shown in repo).