---
### ADR-002: Containerization for Service Deployment and Orchestration

**Status:** Inferred
**Context:** The application consists of multiple services (frontend, backend, and a reverse proxy) that need a consistent and reproducible runtime environment. Managing dependencies and configurations for each service across different developer machines and deployment environments can be complex and error-prone.
**Decision:** Each service is containerized using Docker. A `Dockerfile` is present for the `frontend`, `backend`, and `nginx` services. A `docker-compose.yml` file is used to define and orchestrate these multi-container services, particularly for local development.
**Consequences:**
*   **Positive:**
    *   Guarantees a consistent environment, eliminating "it works on my machine" issues.
    *   Simplifies the developer onboarding and setup process to a single `docker-compose up` command.
    *   Isolates service dependencies, preventing conflicts between them.
*   **Negative:**
    *   Adds a layer of abstraction that developers need to understand.
    *   Introduces a small overhead in terms of disk space for Docker images and performance for the virtualization layer.