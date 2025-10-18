---
### ADR-006: Authentication with JWT and password hashing using bcrypt

Status: Inferred
Context: requirements include PyJWT and bcrypt; frontend has Login/SignUp/OTP components and role-based dashboards.
Decision: Implement stateless authentication with JWT tokens and store password hashes with bcrypt.
Consequences:
- Positive: Scales well across stateless API instances; interoperable with SPA; standard security posture for password storage.
- Negative: Token storage on the client must be secured; token revocation is non-trivial; requires CORS and CSRF considerations.