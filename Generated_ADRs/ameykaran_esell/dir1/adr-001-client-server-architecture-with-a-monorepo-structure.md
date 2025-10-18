### ADR-001: Client-Server Architecture with a Monorepo Structure

**Status:** Inferred
**Context:** The application requires both a user-facing interface for interaction and file uploads, and a powerful backend for data processing, AI integration, and media generation. There is a need to manage both codebases cohesively during development.
**Decision:** A client-server architecture was chosen, separating the system into a `frontend` and a `backend`. Both codebases are maintained within a single root repository. The frontend is responsible for the user interface and user experience, while the backend handles all business logic, file processing, and communication with external services.
**Consequences:**
*   **Positive:**
    *   **Separation of Concerns:** Decouples the UI logic (frontend) from the business and data processing logic (backend), allowing for independent development, scaling, and technology stack choices for each part.
    *   **Simplified Management:** Housing both in a monorepo simplifies initial project setup, version control, and cross-cutting changes.
*   **Negative:**
    *   The build and deployment processes for the frontend and backend are distinct and must be managed separately, despite being in the same repository.
    *   As the project grows, the monorepo could become complex to navigate without proper tooling.