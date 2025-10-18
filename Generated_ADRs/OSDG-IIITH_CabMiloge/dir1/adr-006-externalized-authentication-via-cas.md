---
### ADR-006: Externalized Authentication via CAS

**Status:** Inferred
**Context:** The application requires a secure and reliable method for user authentication. Building a custom authentication and user management system is complex, time-consuming, and carries security risks.
**Decision:** The application integrates with an external Central Authentication Service (CAS) for user authentication. This is inferred from the presence of the `python-cas` library in the `requirements.txt` file. This choice suggests delegation of user sign-on to a pre-existing, trusted identity provider (e.g., from a university or enterprise environment).
**Consequences:**
*   **Positive:**
    *   Reduces development effort and security burden by offloading user authentication to a specialized service.
    *   Enables Single Sign-On (SSO), allowing users to log in with their existing institutional credentials, which improves the user experience.
    *   Centralizes user management outside of the application itself.
*   **Negative:**
    *   Creates a hard dependency on the external CAS provider; if the CAS service is down, users cannot log in to the application.
    *   Introduces potential network latency during the authentication process.
    *   The application is tightly coupled to the CAS protocol and a specific identity provider.