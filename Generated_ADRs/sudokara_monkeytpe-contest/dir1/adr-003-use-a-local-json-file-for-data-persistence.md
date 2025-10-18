---
### ADR-003: Use a Local JSON File for Data Persistence

**Status:** Inferred
**Context:** The application requires a way to store persistent data, specifically for a leaderboard feature. The architectural challenge was to select a data storage mechanism that was simple to implement, required no external dependencies or services, and was sufficient for the application's needs. Setting up a relational database like SQLite or a client-server database would introduce significant complexity for what appears to be a small-scale data storage requirement.
**Decision:** A simple, file-based persistence strategy was chosen using a local JSON file (`leaderboard.json`). The application logic reads from and writes to this file to manage leaderboard data.
**Consequences:**
*   **Positive:**
    *   **Simplicity:** This approach is extremely easy to implement, requiring only standard file system read/write operations available through Node.js.
    *   **Zero-Dependency:** It requires no external database engine, server, or additional libraries, keeping the application lightweight and self-contained.
    *   **Human-Readable:** The data is stored in a plain text format that is easy to inspect, debug, and even manually edit if necessary.
*   **Negative:**
    *   **Not Scalable:** This method is unsuitable for large amounts of data, as the entire file must be read into memory, parsed, and rewritten for every modification.
    *   **Lacks Database Features:** It offers no support for transactions, indexing, or complex queries.
    *   **Prone to Corruption:** The file could become corrupted if the application crashes during a write operation. It is also susceptible to race conditions if not handled carefully, though this is less of a risk in this simple application context.