### ADR-001: Microservices Architecture

**Status:** Inferred
**Context:** The application appears to manage a complex workflow involving a user-facing frontend, model management, service registration, and deployment orchestration. A monolithic architecture would make it difficult to develop, deploy, and scale these distinct functional areas independently. The system required a design that promotes separation of concerns and independent lifecycle management for its components.
**Decision:** The system was designed using a microservices architectural style. The codebase is broken down into multiple, single-responsibility services, each in its own directory. Key services identified include: `frontend`, `api-gateway`, `controller-Service`, `agent-Service`, `deployer-service`, `model-registry`, and `service-registry`.
**Consequences:**
*   **Positive:**
    *   Services can be developed, deployed, and scaled independently.
    *   Clear separation of concerns, improving maintainability.
    *   Enables technology diversity, although most services appear to use a similar stack.
*   **Negative:**
    *   Increased operational complexity due to the number of moving parts.
    *   Requires infrastructure for inter-service communication, service discovery, and centralized configuration.
    *   End-to-end testing is more complex than in a monolith.