---
### ADR-007: Provide Database Administration via a Sidecar sqlite-web Service

Status: Inferred
Context: A second service, sqliteweb, is built from Dockerfile-sqliteweb and shares the database volume. This pattern provides a browser-based UI for the SQLite database.
Decision: Run sqlite-web as a sidecar container sharing the database volume to inspect/manage data.
Consequences: Improves developer and operator ergonomics for troubleshooting and data inspection. If exposed without authentication or network isolation, it can pose security risks. It also couples admin access to the on-disk file, which may be sensitive in production.