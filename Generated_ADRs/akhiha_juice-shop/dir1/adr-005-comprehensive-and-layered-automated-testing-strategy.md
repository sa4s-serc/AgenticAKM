---
### ADR-005: Comprehensive and Layered Automated Testing Strategy

**Status:** Inferred
**Context:** To maintain high quality and stability in a complex full-stack application, manual testing is insufficient. An automated testing strategy is required to validate the functionality of the backend API, the frontend UI, and their interactions.
**Decision:** A multi-layered automated testing strategy has been implemented.
*   **API/Integration Testing:** The `test/api/` directory and the `frisby` script in `package.json` (which runs Jest) indicate the use of automated tests to validate the REST API endpoints.
*   **End-to-End (E2E) Testing:** The `test/cypress/` directory and `cypress.config.ts` show that Cypress is used for E2E testing, simulating real user interactions with the application in a browser.
*   **Smoke Testing:** A `test/smoke/` directory with its own `Dockerfile` suggests the use of lightweight tests to quickly verify that the application is running correctly after a deployment.
**Consequences:**
*   **Positive:**
    *   Provides a strong safety net against regressions, allowing developers to refactor and add new features with confidence.
    *   Enforces quality gates within the CI/CD pipeline, preventing buggy code from reaching production.
    *   The different layers of testing ensure that both individual components and complete user flows are working as expected.
*   **Negative:**
    *   Writing and maintaining a comprehensive test suite requires significant development effort.
    *   E2E tests can be slow and sometimes brittle, potentially increasing the runtime of the CI pipeline.