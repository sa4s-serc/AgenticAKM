---
### ADR-006: Persist Data with SQLite Backed by a Bind-Mounted Host Directory

Status: Inferred
Context: Both services mount ./sqllite_volume to /app/sqllite_volume, implying a local SQLite database file. No external DB drivers are listed in requirements, aligning with Python’s built-in sqlite3 module.
Decision: Use SQLite for persistence, storing the database file on a host-mounted path (bind mount).
Consequences: Simple setup, zero external dependencies, and easy portability/backups. SQLite has limitations under concurrent writes and is less suitable for high-scale or multi-writer scenarios. File-based persistence requires careful handling in containerized environments to avoid corruption during simultaneous access.