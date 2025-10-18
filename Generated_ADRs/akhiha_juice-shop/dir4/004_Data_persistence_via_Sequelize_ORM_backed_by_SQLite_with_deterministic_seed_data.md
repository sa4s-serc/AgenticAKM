# ADR-004: Data persistence via Sequelize ORM backed by SQLite with deterministic seed data

**Date**: 2025-10-10
**Status**: Proposed

## Context
The app must be easy to set up anywhere (workshops, CI, Docker) and ship with known datasets for challenges.

## Decision
Use Sequelize with sqlite3 as the default datastore and seed from data/static (YAML/TS) via datacreator/datacache utilities; keep auxiliary data utilities (e.g., mongodb.ts) available but not primary.

## Consequences
Benefits: zero external dependencies, fast startup, reproducible data for tests and challenges. Drawbacks: limited concurrency and scalability, less representative of production RDBMS behavior, harder migrations if switching databases later.