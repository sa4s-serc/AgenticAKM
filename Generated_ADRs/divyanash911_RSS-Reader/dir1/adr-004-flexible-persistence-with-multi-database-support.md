---
### ADR-004: Flexible Persistence with Multi-Database Support

**Status:** Inferred
**Context:** The application required a data persistence strategy that would be flexible enough for different environments. This includes needing a lightweight, easy-to-configure database for development and testing, as well as a more robust, production-grade database for deployment.
**Decision:** The architecture is designed to support multiple relational databases. The `pom.xml` explicitly includes dependencies for both HSQLDB (`org.hsqldb.hsqldb`), a lightweight in-memory/file-based database, and PostgreSQL (`org.postgresql.postgresql`), a powerful open-source production database.
**Consequences:**
*   **Positive:**
    *   Facilitates easier development and faster, isolated testing using HSQLDB.
    *   Provides a clear path to a scalable and robust production environment with PostgreSQL.
    *   Implies the use of a data abstraction layer (like JDBC or an ORM) which prevents vendor lock-in.
*   **Negative:**
    *   The application must be continuously tested against all supported databases to ensure compatibility.
    *   The data access layer must avoid using proprietary, database-specific SQL features.