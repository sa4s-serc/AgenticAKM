---
### ADR-006: Build the backend with Express 5, ECMAScript modules, and a layered structure (routes/controllers/models/middlewares)

Status: Inferred
Context: Server uses "type": "module", express ^5.1.0, and organized folders for routes, controllers, models, and middlewares.
Decision: Implement an Express 5 API using ESM and a conventional layered architecture.
Consequences:
- Positive: Familiar, testable structure; clear boundaries; async-friendly Express 5; modern ESM.
- Negative: No opinionated framework conventions (e.g., NestJS); more manual wiring; error handling and structure discipline needed.