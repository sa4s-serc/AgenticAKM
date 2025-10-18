---
### ADR-002: Containerization for Environment Consistency and Deployment

**Status:** Inferred
**Context:** The microservices architecture, with its diverse set of technologies (Node.js, Python, Java-based ELK stack) and extensive dependencies, creates a significant challenge in ensuring consistent environments across development, testing, and production. Manual setup would be error-prone and time-consuming.
**Decision:** Use Docker to containerize each service, and `docker-compose` to define and orchestrate the multi-service application. Each service has its own `Dockerfile` specifying its base image and dependencies, and the `docker-compose.yml` file defines how these services connect and run together.
**Consequences:**
*   **Positive:** Provides a high degree of environment consistency and reproducibility, drastically simplifying the setup process for new developers. Isolates service dependencies, preventing conflicts. Streamlines the deployment pipeline and simplifies scaling individual services.
*   **Negative:** Adds a layer of abstraction that requires developer familiarity with Docker concepts. Container images can consume considerable disk space. There is a minor performance overhead associated with containerization compared to running services directly on a host machine.