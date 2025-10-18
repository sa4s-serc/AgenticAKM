---
### ADR-006: JWT for Stateless Authentication

**Status:** Inferred

**Context:** The system required a secure method to manage user sessions and protect API routes. The solution needed to be suitable for a decoupled architecture where the client and server are separate, and it should not require the server to store session state.

**Decision:** A stateless authentication mechanism using JSON Web Tokens (JWT) was implemented. The backend's `package.json` includes `jsonwebtoken` for creating and verifying tokens and `bcrypt` for hashing passwords. The presence of `backend/middleware/auth.js` indicates that this logic is applied as middleware to protect specific API endpoints.

**Consequences:**
*   **Positive:**
    *   The server remains stateless, which simplifies scaling the backend across multiple instances.
    *   JWTs are self-contained and work well across different services and domains, fitting the decoupled architecture.
    *   Using `bcrypt` for password hashing is a critical security measure that protects user credentials.
*   **Negative:**
    *   Once issued, a JWT is valid until it expires and cannot be easily revoked on the server side. Implementing a token denylist is required for immediate session invalidation.
    *   The token must be stored securely on the client to mitigate the risk of XSS attacks stealing the token.