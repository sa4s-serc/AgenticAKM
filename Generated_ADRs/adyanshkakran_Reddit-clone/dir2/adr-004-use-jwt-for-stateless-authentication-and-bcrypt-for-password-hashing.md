---
### ADR-004: Use JWT for stateless authentication and bcrypt for password hashing

Status: Inferred
Context: Backend dependencies include jsonwebtoken and bcrypt, and login/user routes are present.
Decision: Authenticate users with stateless JWT tokens and secure passwords with bcrypt hashing.
Consequences:
- Positive: Scalable stateless auth; interoperable tokens; strong password security.
- Negative: Requires secure token storage and rotation strategies; risk of token leakage; added complexity for token verification and refresh.