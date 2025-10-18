---
### ADR-006: Automation of CI/CD with GitLab CI

**Status:** Inferred
**Context:** Manually building, testing, and deploying the application is time-consuming, error-prone, and not scalable. An automated process is needed to ensure rapid and reliable delivery of new versions.
**Decision:** A Continuous Integration and Continuous Deployment (CI/CD) pipeline has been implemented using GitLab CI, as evidenced by the presence of the `.gitlab-ci.yml` file in the repository root.
**Consequences:**
*   **Positive:**
    *   Every commit can be automatically built and tested, providing fast feedback to developers.
    *   Automates the release process, making deployments faster, more reliable, and repeatable.
    *   Centralizes the definition of the build and deployment process as code, making it version-controlled and transparent.
*   **Negative:**
    *   Creates a dependency on the GitLab CI platform.
    *   Requires specialized knowledge to write and maintain the `.gitlab-ci.yml` configuration file.