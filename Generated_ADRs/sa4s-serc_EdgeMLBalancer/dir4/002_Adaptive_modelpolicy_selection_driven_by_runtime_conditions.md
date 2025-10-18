# ADR-002: Adaptive model/policy selection driven by runtime conditions

**Date**: 2025-10-10
**Status**: Proposed

## Context
README describes selecting models at runtime based on device, battery, and CPU conditions; the UI displays inference-time metrics.

## Decision
Implement dynamic selection of models or configurations based on live system metrics to balance accuracy, latency, and energy.

## Consequences
Improves user-perceived performance across heterogeneous devices but introduces policy complexity, risk of oscillations, and a need for robust telemetry, tuning, and test coverage.