# ADR-006: Persistence with Spring Data JPA/Hibernate and PostgreSQL

**Date**: 2025-10-16
**Status**: Proposed

## Context
The application needs relational persistence with strong ecosystem support and production-ready reliability.

## Decision
Use spring-boot-starter-data-jpa backed by Hibernate, with PostgreSQL as the runtime database and the official JDBC driver.

## Consequences
Accelerates development through ORM abstractions and Spring Data integrations; enables portable domain models; may hide complex SQL behavior and impacts performance if mappings/queries aren’t tuned; ties runtime to a PostgreSQL instance.