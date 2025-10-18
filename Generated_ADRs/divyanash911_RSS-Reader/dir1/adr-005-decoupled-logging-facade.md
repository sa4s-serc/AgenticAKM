---
### ADR-005: Decoupled Logging Facade

**Status:** Inferred
**Context:** In a project with multiple modules and third-party dependencies, different components might use different logging frameworks. There was a need to consolidate logging configuration and output into a single, manageable system without forcing all dependencies to use the same logging implementation.
**Decision:** Use the SLF4J (Simple Logging Facade for Java) API as the standard for logging within the application. The presence of `org.slf4j`, `log4j`, and `jcl-over-slf4j` dependencies indicates that SLF4J is used to abstract away the underlying logging implementation (Log4j), while also redirecting logging from other frameworks.
**Consequences:**
*   **Positive:**
    *   The underlying logging framework can be changed at deployment time with minimal configuration changes and no code modification.
    *   Provides a consistent logging API across the entire codebase.
    *   Improves maintainability by centralizing logging configuration.
*   **Negative:**
    *   Adds a small layer of indirection and an extra dependency to manage.