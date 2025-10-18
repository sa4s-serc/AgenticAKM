---
### ADR-007: Support PostgreSQL version differences via query alternatives

Status: Inferred
Context: pg_query_alts.c and ext_query_alts.c suggest an abstraction to choose queries based on server version/capabilities.
Decision: Implement a query alternative mechanism to pick appropriate SQL statements depending on PostgreSQL version or feature availability.
Consequences:
- Positive: Smooth compatibility across PostgreSQL releases; reduces code forks.
- Negative: Increases testing matrix and complexity of configuration; risk of drift across versions.