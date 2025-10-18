### ADR-001: Selection of Core Framework and Language

**Status:** Inferred

**Context:** The project required a robust, scalable, and maintainable backend service. A foundational decision was needed for the primary programming language and application framework to ensure rapid development, dependency management, and support for web and data access capabilities.

**Decision:** The project is built using the **Java** language (specifically version 21) on the **Spring Boot** framework. **Maven** is used as the build automation and dependency management tool. This is evidenced by the `pom.xml` file, which specifies a `spring-boot-starter-parent`, a `<java.version>21</java.version>` property, and dependencies like `spring-boot-starter-web`. The presence of `mvnw` and `mvnw.cmd` further confirms the choice of Maven.

**Consequences:**
*   **Positive:**
    *   Leverages the extensive Java and Spring ecosystem, providing a wide range of libraries and community support.
    *   Spring Boot's opinionated auto-configuration and starter dependencies significantly accelerate setup and development time.
    *   Enables the creation of standalone, production-grade applications with minimal boilerplate code.
    *   Maven provides a standardized build lifecycle and simplifies dependency management across the project.
*   **Negative:**
    *   Spring Boot applications can have a larger memory footprint and slower startup time compared to some lighter-weight frameworks.
    *   The "magic" of auto-configuration can sometimes make it difficult to debug or override default behaviors.