---
### ADR-006: Continuous Integration for Automated Builds

**Status:** Inferred
**Context:** To maintain code quality, ensure that the project builds correctly, and get rapid feedback on changes, an automated build and test process was necessary.
**Decision:** The project uses Travis CI for its Continuous Integration (CI) pipeline. This is directly evidenced by the presence of the `.travis.yml` file in the repository root, which is the configuration file for the Travis CI service.
**Consequences:**
*   **Positive:**
    *   Automates the build and test process, reducing the risk of human error.
    *   Provides immediate feedback to developers when a commit breaks the build or tests.
    *   Enforces a consistent development process and improves overall code quality.
*   **Negative:**
    *   Creates a dependency on an external service (Travis CI).
    *   Build failures on the CI server can temporarily block development progress until they are fixed.