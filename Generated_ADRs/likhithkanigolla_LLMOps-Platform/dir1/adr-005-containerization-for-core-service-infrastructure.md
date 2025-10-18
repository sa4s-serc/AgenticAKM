---
### ADR-005: Containerization for Core Service Infrastructure

**Status:** Inferred
**Context:** To ensure consistency and simplify the deployment of the system's core services and their dependencies, a standardized packaging and runtime environment was needed.
**Decision:** Use **Docker** for containerization. Evidence for this includes the `docker` Python library in several `requirements.txt` files (allowing services to interact with the Docker daemon) and the presence of a `docker-compose.yaml` file for setting up the Kafka infrastructure. It is highly probable that the microservices themselves are also intended to be run as Docker containers.
**Consequences:**
*   **Positive:**
    *   Ensures that services run in a consistent and reproducible environment across development and production.
    *   Simplifies dependency management for complex infrastructure like Kafka.
    *   Streamlines the local development setup process.
*   **Negative:**
    *   Adds a layer of abstraction and requires developers to be familiar with Docker concepts.
    *   The reliance on bootstrap shell scripts (`.sh`) instead of a more declarative orchestration tool like Kubernetes suggests that the deployment and management process may be semi-manual or simplistic.