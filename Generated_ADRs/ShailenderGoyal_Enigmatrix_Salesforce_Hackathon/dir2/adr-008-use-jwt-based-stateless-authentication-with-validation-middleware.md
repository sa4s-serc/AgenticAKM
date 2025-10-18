---
### ADR-008: Use JWT-based stateless authentication with validation middleware

Status: Inferred
Context: Dependencies include jsonwebtoken and joi, and there are auth-related middlewares (authEnsure, authValidation) and controller/routes for auth.
Decision: Implement stateless authentication using JWTs, with Joi for payload validation and middleware for enforcement.
Consequences:
- Positive: Horizontally scalable auth; simple integration with SPA; no server session storage.
- Negative: Token storage/refresh flows must be secured; JWT invalidation is non-trivial; clock skew and expiry handling needed.