---
### ADR-004: Development Environment and Database Provisioning

**Status:** Inferred

**Context:** The project needed a consistent, reproducible, and isolated development environment, particularly for external services like the database. A mechanism was also required to initialize the database schema and populate it with sample data automatically.

**Decision:** **Docker and Docker Compose** are used to manage the development environment, specifically for the PostgreSQL database. The `docker-compose.yml` file defines the `postgres` service. Furthermore, database schema creation and data seeding are automated by mounting local SQL scripts (`./src/main/resources/sql`) into the container's initialization directory (`/docker-entrypoint-initdb.d`), as seen in the `volumes` configuration.

**Consequences:**
*   **Positive:**
    *   Developers can set up the entire database environment with a single command (`docker-compose up`), ensuring consistency across all machines.
    *   Isolates the database from the host operating system, avoiding conflicts with other locally installed software.
    *   Automating schema and data initialization streamlines the setup process for new developers and ensures a clean state for testing.
*   **Negative:**
    *   Adds a dependency on Docker, requiring developers to install it and have a basic understanding of its concepts.
    *   This initialization method is primarily for the first run of the container; subsequent database schema changes (migrations) would require a different strategy.