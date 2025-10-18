---
### ADR-005: Lightweight Database Persistence with SQLite

**Status:** Inferred
**Context:** The backend service needed a persistent storage solution to manage data such as conversation state, user information, or logs. The requirements likely favored simplicity, zero-configuration setup, and ease of deployment over high-concurrency write performance or distributed scaling.
**Decision:** SQLite was chosen as the database for the backend. This is inferred from the `db-sqlite3` dependency in `requirements.txt`, the presence of a `schema.sql` file for defining tables, `db.py` for database interactions, and a file named `threads_db` which is likely the SQLite database file itself.
**Consequences:**
*   **Positive:**
    *   **Simplicity:** SQLite is serverless and self-contained. The entire database is a single file, making it extremely easy to set up, back up, and deploy.
    *   **Zero-Configuration:** There is no separate database server to install, manage, or configure.
    *   **Good Performance for Read-Heavy Loads:** It performs very well for applications with low to medium traffic and where writes are not highly concurrent.
*   **Negative:**
    *   **Limited Concurrency:** SQLite is not well-suited for applications with a high volume of concurrent writes, as it locks the entire database file during a write operation.
    *   **Not for Distributed Systems:** It is not a client-server database and cannot be easily scaled across multiple application servers.