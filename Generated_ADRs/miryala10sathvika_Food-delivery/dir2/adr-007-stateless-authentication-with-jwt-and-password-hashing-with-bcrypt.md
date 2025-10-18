---
### ADR-007: Stateless authentication with JWT and password hashing with bcrypt

Status: Inferred
Context: jsonwebtoken present; backend/middleware/auth.js; user model/controller; bcrypt and bcryptjs are both dependencies.
Decision: Authenticate via JWT tokens; hash passwords with bcrypt (with bcryptjs available as fallback/alt).
Consequences:
- Positive: Stateless, horizontal scaling-friendly; widely supported on clients; secure password storage.
- Negative: Token revocation is non-trivial; token storage on clients must be secured; dual bcrypt libs can confuse maintenance.