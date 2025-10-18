---
### ADR-004: Implement PostgreSQL protocol directly instead of using libpq

Status: Inferred
Context: There is no libpq dependency. Files like message.c, connection.c, server.c, queries.c suggest a direct implementation of the PostgreSQL wire protocol and query handling.
Decision: Implement the PostgreSQL frontend/backend protocol natively to query metrics without libpq.
Consequences:
- Positive: Reduces external dependencies; tighter control over connection behavior; potential performance gains.
- Negative: Protocol maintenance burden; must track PostgreSQL protocol changes; increased testing requirements.