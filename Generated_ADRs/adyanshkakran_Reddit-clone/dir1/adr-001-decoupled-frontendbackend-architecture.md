### ADR-001: Decoupled Frontend/Backend Architecture

**Status:** Inferred
**Context:** The application requires a clear separation between the user interface (presentation logic) and the server-side business logic and data management. This separation is crucial for allowing independent development, deployment, and scaling of the two distinct parts of the system.
**Decision:** The application is structured into two separate services: a `frontend` service and a `backend` service. The frontend is a Single-Page Application (SPA) that communicates with the backend via an API. The `backend` folder contains a Node.js/Express application, while the `frontend` folder contains a React application.
**Consequences:**
*   **Positive:**
    *   Enables parallel development, as frontend and backend teams can work independently against a defined API contract.
    *   Allows for technology stack specialization (React/TypeScript for the frontend, Node.js/Express for the backend).
    *   The frontend and backend can be scaled independently based on their specific resource needs.
*   **Negative:**
    *   Increases operational complexity, as two separate services must be built, deployed, and managed.
    *   Requires careful management of the API contract between the services.
    *   Cross-Origin Resource Sharing (CORS) must be correctly configured on the backend, as evidenced by the `cors` dependency.