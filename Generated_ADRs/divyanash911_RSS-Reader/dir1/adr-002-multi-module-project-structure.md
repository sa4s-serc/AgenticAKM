---
### ADR-002: Multi-Module Project Structure

**Status:** Inferred
**Context:** The application, "Reader," likely has multiple distinct functional areas (e.g., core logic, web API, persistence). A single, monolithic structure would make the codebase harder to manage, maintain, and scale as it grows.
**Decision:** The project is structured as a multi-module Maven project. The `pom.xml` provided is for a `reader-parent` artifact with `<packaging>pom</packaging>`, which is the standard convention for a parent module that aggregates and manages sub-modules.
**Consequences:**
*   **Positive:**
    *   Enforces a clear separation of concerns, leading to better organization and maintainability.
    *   Allows for independent development and testing of different modules.
    *   Promotes code reuse by defining shared dependencies and properties in the parent POM.
*   **Negative:**
    *   Can introduce additional complexity in the build configuration and inter-module dependencies.
    *   Initial setup is more involved than a single-module project.