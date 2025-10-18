### ADR-001: Monorepo for Code Organization

**Status:** Inferred

**Context:** The project is composed of three distinct but interconnected applications: a user-facing frontend, an administrative frontend, and a backend API. Managing these as separate repositories would create overhead in coordinating changes, managing dependencies, and ensuring consistency across the different parts of the system.

**Decision:** A monorepo structure was adopted to house all three applications (`frontend`, `admin`, `backend`) within a single Git repository. This allows for unified version control and simplifies cross-cutting changes.

**Consequences:**
*   **Positive:**
    *   Simplifies dependency management and reduces code duplication.
    *   Enables atomic commits that span multiple parts of the application (e.g., an API change in the backend and the corresponding UI change in the frontend).
    *   Provides full visibility of the entire system to all developers, potentially improving collaboration.
    *   Streamlines the onboarding process for new developers who only need to clone a single repository.
*   **Negative:**
    *   The repository can become very large over time, potentially slowing down Git operations.
    *   Continuous integration and deployment pipelines can become more complex, requiring logic to build and deploy only the components that have changed.
    *   Without clear boundaries, there is a risk of creating tight coupling between the applications.