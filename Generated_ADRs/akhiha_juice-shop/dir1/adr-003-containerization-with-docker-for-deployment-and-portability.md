---
### ADR-003: Containerization with Docker for Deployment and Portability

**Status:** Inferred
**Context:** To ensure the application runs consistently across different environments (development, testing, production) and is easily distributable, a standardized deployment strategy was necessary. Furthermore, minimizing the security footprint of the production deployment is a critical concern.
**Decision:** The application is containerized using Docker. A multi-stage `Dockerfile` is used to create an optimized and secure production image. The build process first installs dependencies and builds the application in a full Node.js image, then copies the final artifacts into a minimal `gcr.io/distroless/nodejs20-debian11` base image.
**Consequences:**
*   **Positive:**
    *   **Consistency:** The application runs in the same environment everywhere, eliminating "it works on my machine" problems.
    *   **Security:** The use of a distroless base image significantly reduces the attack surface of the production container by removing shells, package managers, and other unnecessary utilities.
    *   **Efficiency:** Multi-stage builds result in a smaller final image size, which is faster to pull and deploy.
    *   **DevOps:** Simplifies the CI/CD pipeline, as the final build artifact is a self-contained, runnable Docker image. The presence of `docker-compose.test.yml` and `test/smoke/Dockerfile` indicates containerization is also leveraged for testing.
*   **Negative:**
    *   Adds a layer of abstraction that requires developers and operators to have a working knowledge of Docker.
    *   Debugging can be more difficult inside a minimal, distroless container.