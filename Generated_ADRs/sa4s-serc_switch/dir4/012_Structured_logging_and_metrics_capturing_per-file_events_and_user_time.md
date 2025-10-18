# ADR-012: Structured logging and metrics capturing per-file events and user time

**Date**: 2025-10-10
**Status**: Proposed

## Context
The system must support performance auditing, SLO evaluation, and adaptation traceability.

## Decision
Emit JSON logs with per-file processing events, timestamps, selected model variant, and user request time; export scenario-level metrics as CSV.

## Consequences
Facilitates post-hoc analysis and comparisons across runs; easy to ingest into analytics tools; lacks standardized tracing/metrics protocols and real-time dashboards without additional tooling.