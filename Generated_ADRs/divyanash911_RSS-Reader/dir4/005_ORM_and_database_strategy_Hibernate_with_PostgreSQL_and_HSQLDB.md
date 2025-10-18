# ADR-005: ORM and database strategy: Hibernate with PostgreSQL and HSQLDB

**Date**: 2025-10-13
**Status**: Proposed

## Context
Dependencies include Hibernate ORM and drivers for PostgreSQL and HSQLDB.

## Decision
Use Hibernate for persistence, with PostgreSQL as the primary production database and HSQLDB for development/testing.

## Consequences
Offers robust ORM capabilities and SQL portability; eases local development with an embedded DB; risks behavior drift between HSQLDB and PostgreSQL; necessitates schema migration and tuning practices not shown in this snapshot.