---
### ADR-003: Extensible, Configuration-Driven Metric Collection

**Status:** Inferred

**Context:** PostgreSQL is a highly extensible database with numerous popular extensions like PostGIS, TimescaleDB, and Citus. A hard-coded approach to metric collection would require developers to modify and recompile the C source code every time support for a new extension is added. This would create a tight coupling between the exporter's core logic and the specific metrics being collected, slowing down development and making it difficult for users to add their own custom metrics.

**Decision:** The architecture is designed to be **extensible through external configuration files (YAML)**. The `extensions/` directory contains several `.yaml` files (`postgis.yaml`, `timescaledb.yaml`, etc.) that define the metrics for specific PostgreSQL extensions. The core application parses these files at runtime to dynamically add new metrics to its collection.

**Consequences:**
*   **Positive:**
    *   **Decoupling:** The core exporter engine is decoupled from the specific SQL queries used to gather metrics.
    *   **Flexibility:** Users can easily add support for new PostgreSQL extensions or their own custom application metrics by simply creating a new YAML file, without needing to know C or recompile the application.
    *   **Maintainability:** Metric definitions are kept in simple, human-readable YAML files, making them easier to manage, version, and share.
*   **Negative:**
    *   **Configuration Complexity:** The YAML format for defining metrics could become complex, requiring good documentation (`doc/YAML.md`) to be used effectively.
    *   **Runtime Overhead:** There is a minor performance cost associated with parsing configuration files at startup compared to a fully compiled-in approach.