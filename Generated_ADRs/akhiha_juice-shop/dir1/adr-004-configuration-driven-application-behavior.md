---
### ADR-004: Configuration-Driven Application Behavior

**Status:** Inferred
**Context:** The application is designed to operate in various modes, as suggested by its description ("insecure web application", "ctf", "awareness"). Hardcoding these different behaviors would make the application rigid and difficult to adapt for different training or event scenarios.
**Decision:** The application's behavior is driven by external configuration files. A dedicated `config/` directory contains multiple YAML files (e.g., `default.yml`, `ctf.yml`, `tutorial.yml`, `unsafe.yml`) for different scenarios. A `config.schema.yml` is used to define and validate the structure of these configuration files.
**Consequences:**
*   **Positive:**
    *   **Flexibility:** The application can be easily customized for different use cases without changing the source code.
    *   **Maintainability:** Separates configuration from logic, which is a well-established software engineering best practice.
    *   **Clarity:** The schema provides clear documentation on what configuration options are available and their expected format.
*   **Negative:**
    *   The application's runtime behavior can become less obvious, as it depends heavily on the loaded configuration file, which might complicate debugging.
    *   Poorly managed configurations could lead to unexpected security vulnerabilities or application instability.