---
### ADR-008: Prefer SQL-first schema initialization in local environments

Status: Inferred
Context: There is a need for explicit control over schema creation independent of JPA auto-DDL.
Decision: Supply explicit SQL schema under src/main/resources/sql/schema executed by Postgres at container start, rather than relying solely on Hibernate auto-DDL.
Consequences:
- Positive: Deterministic schema, easier DBA review, parity with production DDL practices.
- Negative: Potential drift if JPA entities change without updating SQL; extra maintenance to keep JPA mappings and SQL synchronized.