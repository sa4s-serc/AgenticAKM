# ADR-010: CSV-based audit logging for events and uploads

**Date**: 2025-10-14
**Status**: Proposed

## Context
Operators need a lightweight, analyzable audit trail without introducing a database dependency.

## Decision
Emit structured CSV logs for observed events (counts, sizes) and uploads (name, cloud ID, timestamp), supplementing standard logs.

## Consequences
Easy ingestion into tools like pandas; human-readable and portable; lacks transactional guarantees and schema enforcement; may not scale to very large volumes; querying is ad hoc.