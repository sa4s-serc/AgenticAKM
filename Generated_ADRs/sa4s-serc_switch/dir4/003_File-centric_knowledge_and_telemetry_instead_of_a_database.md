# ADR-003: File-centric knowledge and telemetry instead of a database

**Date**: 2025-10-10
**Status**: Proposed

## Context
The prototype must be easy to reason about, reproduce, and audit across experiments without operational DB overhead.

## Decision
Persist knowledge (model mappings, monitor data) and telemetry as CSV/JSON files and use the filesystem for inter-component data exchange.

## Consequences
Simple, transparent, and versionable; supports reproducible experiments; limits concurrency and transactional integrity; complicates horizontal scaling and rich querying; increases risk of file I/O contention.