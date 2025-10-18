---
### ADR-005: Use HSQLDB for tests/development and PostgreSQL for production

Status: Inferred
Context: The POM includes HSQLDB 2.3.0 and PostgreSQL JDBC 9.4 (jre7) drivers, indicating a lightweight test DB and a production-grade RDBMS.
Decision: Adopt HSQLDB as an embedded/in-memory database for tests and PostgreSQL as the production database.
Consequences:
- Positive: Fast, deterministic tests; robust production capabilities with PostgreSQL.
- Negative: Behavioral differences between HSQLDB and PostgreSQL can cause environment-specific issues; older JDBC driver may miss newer features/performance improvements.