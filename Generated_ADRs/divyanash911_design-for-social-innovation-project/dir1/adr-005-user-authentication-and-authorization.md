---
### ADR-005: User Authentication and Authorization

**Status:** Inferred
**Context:** The application needs a secure way to manage user sessions, particularly for a decoupled architecture where the frontend and backend are separate. The system must authenticate users and authorize their access to different parts of the application (e.g., `ParentDashboard`, `TeacherDashboard`, `PsychologistDashboard`). A stateless mechanism is preferred to simplify backend scaling.
**Decision:** A token-based authentication system using JSON Web Tokens (JWT) was implemented. This is inferred from the inclusion of `PyJWT` for token generation/validation and `bcrypt` for securely hashing passwords in the backend's `requirements.txt`.
**Consequences:**
*   **Positive:**
    *   The backend remains stateless, as the JWT contains all necessary information to authenticate a user. This improves scalability.
    *   JWTs work well with decoupled architectures and cross-origin (CORS) requests.
    *   Password security is enhanced by using `bcrypt` for hashing, protecting against rainbow table and brute-force attacks.
*   **Negative:**
    *   JWTs, once issued, cannot be easily invalidated before their expiration. A token revocation system (e.g., a blacklist) would need to be implemented for immediate session termination, adding state back into the system.
    *   Care must be taken to securely store the JWT on the client-side to prevent Cross-Site Scripting (XSS) attacks.