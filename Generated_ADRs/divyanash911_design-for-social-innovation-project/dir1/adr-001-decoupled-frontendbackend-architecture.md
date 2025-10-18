### ADR-001: Decoupled Frontend/Backend Architecture

**Status:** Inferred
**Context:** The application requires a clear separation between the user interface (presentation layer) and the server-side logic (business and data layers). This separation is necessary to allow for independent development, deployment, and scaling of the two components. The system needs to serve a dynamic, interactive user experience while managing data persistence and business rules on a server.
**Decision:** A decoupled, client-server architecture was chosen. The frontend is a Single Page Application (SPA) built with React, and the backend is a RESTful API built with Python and the Flask framework. The two communicate over HTTP. The presence of `Flask-Cors` in `requirements.txt` explicitly confirms the need to handle cross-origin requests between these two separate domains (or ports during development).
**Consequences:**
*   **Positive:**
    *   Enables parallel development, allowing frontend and backend teams to work independently against a defined API contract.
    *   The technology stack for the frontend (React) and backend (Python/Flask) can be chosen independently, leveraging the best tools for each job.
    *   Allows for independent scaling; if the backend is under heavy load, it can be scaled without affecting the frontend, and vice-versa.
*   **Negative:**
    *   Introduces complexity in managing the interaction between two separate applications (e.g., CORS configuration, API versioning).
    *   Adds network latency for all data-related operations, as every request must travel from the client to the server.
    *   Requires a more complex deployment and operational setup compared to a monolithic application.