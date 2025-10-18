# ADR-008: Startup Data Seeding via CommandLineRunner with SQL Scripts

**Date**: 2025-10-16
**Status**: Proposed

## Context
Local development and first-time deployments benefit from pre-populated data and deterministic schema setup.

## Decision
Run a DataInitializer at startup that waits briefly for the database, checks for an empty questions table, and loads sample data from SQL files using JdbcTemplate while skipping comments and tolerating duplicates.

## Consequences
Improves developer experience and idempotency; reduces manual steps; startup time increases slightly; logic must remain careful to avoid partial loads; suitability for production depends on data governance policies.