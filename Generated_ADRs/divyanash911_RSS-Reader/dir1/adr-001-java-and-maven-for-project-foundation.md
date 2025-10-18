### ADR-001: Java and Maven for Project Foundation

**Status:** Inferred
**Context:** The project required a mature, cross-platform programming language and a robust build and dependency management system. The goal was to create a stable, maintainable application with access to a wide ecosystem of libraries.
**Decision:** The project is built using the Java programming language (specifically targeting version 1.8), and Apache Maven is used for build automation and dependency management. The `pom.xml` file is the central piece of evidence for this, defining the project structure, dependencies, and build lifecycle.
**Consequences:**
*   **Positive:**
    *   Leverages the extensive and mature Java ecosystem of libraries and frameworks.
    *   Maven provides a standardized, declarative build process, making it easier for new developers to understand and build the project.
    *   Dependency management is centralized and simplified.
*   **Negative:**
    *   Java can be more verbose compared to other modern languages.
    *   Maven's XML-based configuration can become complex for very large projects.