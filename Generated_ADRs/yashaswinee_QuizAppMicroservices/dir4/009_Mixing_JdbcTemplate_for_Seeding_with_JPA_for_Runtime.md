# ADR-009: Mixing JdbcTemplate for Seeding with JPA for Runtime

**Date**: 2025-10-16
**Status**: Proposed

## Context
Schema and data bootstrap are simpler with raw SQL, while runtime CRUD benefits from ORM conveniences.

## Decision
Use JdbcTemplate to execute SQL scripts for schema/data seeding, and use JPA/Hibernate for application operations.

## Consequences
Provides pragmatic control over initialization while keeping runtime logic high-level; introduces two data access paradigms to maintain; potential drift if SQL seeding and JPA mappings diverge.