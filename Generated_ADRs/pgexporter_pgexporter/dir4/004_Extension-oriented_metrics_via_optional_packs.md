# ADR-004: Extension-oriented metrics via optional packs

**Date**: 2025-10-16
**Status**: Proposed

## Context
Operators commonly deploy PostgreSQL extensions that expose additional observability signals.

## Decision
Provide extension-specific metric packs (e.g., pg_stat_statements, TimescaleDB, Citus, PostGIS, vector, etc.) under a dedicated extensions/ tree.

## Consequences
Out-of-the-box visibility for popular extensions; modular adoption; requires extensions to be installed/enabled and packs kept in sync with extension changes.