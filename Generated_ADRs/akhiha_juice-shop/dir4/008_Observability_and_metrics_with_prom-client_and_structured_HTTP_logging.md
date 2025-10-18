# ADR-008: Observability and metrics with prom-client and structured HTTP logging

**Date**: 2025-10-10
**Status**: Proposed

## Context
Operational insight is needed for demos, CI health checks, and monitoring in containers.

## Decision
Expose Prometheus metrics via prom-client and use morgan for structured request logging; keep health/metrics endpoints accessible.

## Consequences
Benefits: actionable telemetry for performance and availability, simplifies CI smoke tests and demos. Drawbacks: must avoid leaking sensitive data in logs/metrics, metrics endpoints can reveal internals if not controlled.