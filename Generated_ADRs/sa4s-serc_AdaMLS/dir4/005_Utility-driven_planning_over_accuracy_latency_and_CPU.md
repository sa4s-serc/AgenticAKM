# ADR-005: Utility-driven planning over accuracy, latency, and CPU

**Date**: 2025-10-10
**Status**: Proposed

## Context
Service-level goals require optimizing multiple, sometimes conflicting objectives.

## Decision
Define a utility function combining detection confidence/accuracy, response time, and CPU usage; rules select models to maximize expected utility under current context.

## Consequences
Transparent trade-offs and tunable priorities; requires careful weight/threshold calibration; utility drift may occur if workload characteristics change.