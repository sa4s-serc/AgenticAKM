# ADR-008: Lightweight persistence with JDBI and H2 plus connection pooling

**Date**: 2025-10-14
**Status**: Proposed

## Context
The BOM lists JDBI, H2, and pools (C3P0/DBCP).

## Decision
Use JDBI for data access against H2 (and potentially other RDBMS), with pooled connections.

## Consequences
Fast, low-ceremony persistence suitable for embedded/desktop or small servers; limited horizontal scalability and advanced ORM features; dual pool libraries can cause configuration drift if both are present.