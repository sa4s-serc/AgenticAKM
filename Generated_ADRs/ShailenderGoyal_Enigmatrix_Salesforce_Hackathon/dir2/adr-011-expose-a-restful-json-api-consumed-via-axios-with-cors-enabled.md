---
### ADR-011: Expose a RESTful JSON API consumed via Axios with CORS enabled

Status: Inferred
Context: Frontend uses axios; server uses cors and defines REST-style route files (auth.route.js, chat.route.js, knowledgeBase.route.js, etc.).
Decision: Provide REST endpoints from the Express server and consume them via Axios from the SPA, enabling CORS for cross-origin development.
Consequences:
- Positive: Simple, ubiquitous pattern; easy to integrate with React Query; straightforward debugging.
- Negative: No schema-driven contracts like GraphQL; manual API versioning and pagination patterns required.