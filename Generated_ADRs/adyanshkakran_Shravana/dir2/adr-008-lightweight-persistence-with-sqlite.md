---
### ADR-008: Lightweight persistence with SQLite

Status: Inferred
Context: The presence of db-sqlite3, schema.sql, and a threads_db artifact suggests a simple relational store for conversations/threads. For prototypes and small deployments, SQLite is sufficient.
Decision: Use SQLite as the primary data store for the WhatsApp bot.
Consequences:
- Positive: Zero-setup database, embedded, simple schema management, great for local/dev and small-scale prod.
- Negative: Limited concurrency and scaling; eventual migration needed if write load or multi-instance deployment grows.