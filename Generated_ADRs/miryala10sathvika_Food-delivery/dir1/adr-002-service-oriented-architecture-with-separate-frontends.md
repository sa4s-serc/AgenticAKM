---
### ADR-002: Service-Oriented Architecture with Separate Frontends

**Status:** Inferred

**Context:** The application needs to serve two distinct groups of users: customers and administrators. Each group has different needs, features, and user interfaces. Combining both into a single frontend application would increase its complexity, bundle size, and make it difficult to manage role-specific features.

**Decision:** The system is architected into three separate services:
1.  A central `backend` API that handles all business logic and data persistence.
2.  A `frontend` Single-Page Application (SPA) for customer-facing interactions.
3.  A separate `admin` SPA for administrative and content management tasks.

The two frontend applications are completely decoupled from the backend, communicating with it solely via a defined HTTP API.

**Consequences:**
*   **Positive:**
    *   Strong separation of concerns between the backend logic and the presentation layers.
    *   Allows for independent development, testing, and deployment cycles for each application.
    *   The user-facing `frontend` is not burdened with the code and dependencies of the `admin` panel, leading to better performance.
    *   The backend API can potentially serve other clients in the future (e.g., a native mobile app) without modification.
*   **Negative:**
    *   Increases the number of projects to maintain and deploy.
    *   Requires a well-defined and versioned API contract between the backend and its clients.
    *   Requires proper Cross-Origin Resource Sharing (CORS) configuration on the backend to allow requests from the frontend domains.