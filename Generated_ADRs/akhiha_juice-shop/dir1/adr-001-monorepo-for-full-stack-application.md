### ADR-001: Monorepo for Full-Stack Application

**Status:** Inferred
**Context:** Managing a web application with distinct frontend and backend codebases can introduce complexities. Challenges include keeping API contracts synchronized, managing cross-cutting concerns, and streamlining the build and deployment process for two separate projects. A decision was needed on how to structure the repository to optimize development workflow and maintainability.
**Decision:** The project is structured as a monorepo, containing both the backend Node.js application and the frontend Angular application within a single Git repository. The backend code resides in the root directory (`server.ts`, `routes/`, `models/`) while the frontend code is clearly separated in the `frontend/` directory.
**Consequences:**
*   **Positive:**
    *   Simplifies dependency management and build orchestration, as seen in the root `package.json`'s `postinstall` script which installs frontend dependencies and builds the frontend.
    *   Ensures that frontend and backend changes that depend on each other can be versioned and deployed together within a single commit.
    *   Allows for unified tooling for linting (`.eslintrc.js`), testing, and CI/CD (`.gitlab-ci.yml`) across the entire stack.
*   **Negative:**
    *   The repository size can become large over time.
    *   The build process is more complex, as it has to handle both the backend (TypeScript compilation) and frontend (Angular build) environments.
    *   Clear conventions are required to prevent tight coupling between the frontend and backend codebases.