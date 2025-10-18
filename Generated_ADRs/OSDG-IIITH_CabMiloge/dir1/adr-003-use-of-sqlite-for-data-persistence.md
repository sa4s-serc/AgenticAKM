---
### ADR-003: Use of SQLite for Data Persistence

**Status:** Inferred
**Context:** The application requires a database to store persistent data such as user profiles, journeys, and bookings. The choice of database needed to be simple to manage and integrate within the containerized environment.
**Decision:** SQLite was chosen as the database engine. This is strongly implied by:
1.  The `docker-compose.yml` file defines a `sqliteweb` service, which is a web-based GUI specifically for SQLite databases.
2.  A shared volume (`sqllite_volume`) is mounted to both the application and `sqliteweb` services, which is the standard pattern for file-based databases like SQLite.
3.  The `requirements.txt` file lacks any drivers for other database systems like PostgreSQL, MySQL, or MongoDB.
**Consequences:**
*   **Positive:**
    *   Zero-configuration setup; the database is a simple file within a volume, requiring no separate server process.
    *   Extremely lightweight and portable.
    *   The included `sqliteweb` service provides a convenient way to inspect and manage the database during development.
*   **Negative:**
    *   SQLite does not handle high levels of write concurrency well, which could become a performance bottleneck.
    *   It is not designed for distributed or highly-available setups, limiting the application's scalability.
    *   Features found in client-server databases (e.g., user roles, advanced replication) are not available.