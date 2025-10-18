### ADR-001: Containerization for Environment Consistency

**Status:** Inferred
**Context:** The project requires a consistent and reproducible environment for development and deployment to avoid "it works on my machine" issues. Managing Python versions, system dependencies, and application configuration across different developer machines and deployment targets can be complex and error-prone.
**Decision:** The application and its supporting services are containerized using Docker. Docker Compose is used to define and orchestrate the multi-service environment, which includes the main web application (`cabsharing`) and a database management tool (`sqliteweb`). This is evidenced by the `Dockerfile`, `Dockerfile-sqliteweb`, and `docker-compose.yml` files.
**Consequences:**
*   **Positive:**
    *   Provides a consistent, isolated, and portable runtime environment.
    *   Simplifies the onboarding process for new developers, who only need Docker installed to run the entire stack using `run.sh`.
    *   Dependencies are explicitly managed within the Docker images, ensuring consistency.
*   **Negative:**
    *   Adds a layer of abstraction, which can increase the complexity of debugging.
    *   Introduces a dependency on Docker and Docker Compose tooling.
    *   Container images consume disk space and add a slight performance overhead compared to running directly on the host.