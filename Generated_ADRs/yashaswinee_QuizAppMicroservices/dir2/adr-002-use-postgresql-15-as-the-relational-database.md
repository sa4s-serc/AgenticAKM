---
### ADR-002: Use PostgreSQL 15 as the relational database

Status: Inferred
Context: The application needs a reliable, open-source relational database with strong support in Spring and Docker.
Decision: Choose PostgreSQL 15 as the database, provisioned via Docker (docker-compose.yml), with database name questiondb and credentials admin/password123.
Consequences:
- Positive: Robust SQL features, wide community support, easy integration with Spring Data JPA, simple local setup with Docker.
- Negative: Credentials in compose file are insecure (dev-only); requires Docker for local development; operational knowledge of Postgres needed for production.