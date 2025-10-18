---
### ADR-003: Client-Server Architecture for Separation of Concerns

**Status:** Inferred
**Context:** The system has at least two distinct user interfaces: a rich mobile/web application (`shravana-app`) and a conversational WhatsApp bot (`whatsapp-bot`). These front-facing components need to interact with a central source of logic and data. A monolithic architecture would tightly couple the UI with the business logic, making it difficult to scale or maintain them independently.
**Decision:** The architecture is a client-server model, with a clear separation between the frontend clients (the React Native app) and the backend services (the Python/Flask application). The `shravana-app` and `whatsapp-bot` directories represent distinct components that likely communicate via a web API.
**Consequences:**
*   **Positive:**
    *   **Decoupling:** Frontend and backend teams can develop, test, and deploy their respective components independently.
    *   **Flexibility:** The backend can serve multiple types of clients (mobile app, web app, bots) through the same API, promoting reusability.
    *   **Independent Scaling:** The backend can be scaled to handle increased load without affecting the frontend clients, and vice-versa.
*   **Negative:**
    *   **Increased Complexity:** This architecture introduces network latency and requires a well-defined, versioned API contract between the client and server.
    *   **Operational Overhead:** Managing and deploying two separate applications (frontend and backend) can be more complex than a single monolithic application.