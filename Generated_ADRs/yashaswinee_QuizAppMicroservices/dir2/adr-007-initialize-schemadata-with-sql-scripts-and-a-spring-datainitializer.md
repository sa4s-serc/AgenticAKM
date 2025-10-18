---
### ADR-007: Initialize schema/data with SQL scripts and a Spring DataInitializer

Status: Inferred
Context: Ensure the database has required schema and seed/sample data for local development. Also support application-level setup tasks.
Decision: 
- Provide SQL schema and sample data under src/main/resources/sql executed by Postgres at container initialization.
- Include a Spring bean (DataInitializer) to programmatically insert or prepare data at application startup.
Consequences:
- Positive: Fast onboarding with ready-to-use data; flexibility to add runtime initializations beyond static SQL.
- Negative: Risk of duplication or conflicts between SQL seeding and programmatic initialization; requires idempotent logic and coordination for different environments.