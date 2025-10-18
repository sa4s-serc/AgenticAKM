---
### ADR-003: Provision database via Docker Compose with persistent volume and init SQL

Status: Inferred
Context: Developers need a reproducible, bootstrapped database environment for local development and testing.
Decision: Use docker-compose to run a postgres:15 container; mount src/main/resources/sql to /docker-entrypoint-initdb.d to auto-run schema/data scripts; persist data via a named volume (postgres_data).
Consequences:
- Positive: One-command setup, consistent local environments, schema and sample data seeded automatically, data persists across restarts.
- Negative: Changes to schema/data require container re-creation to reapply init scripts; stateful volumes can hide drift; introduces dependency on Docker for onboarding.