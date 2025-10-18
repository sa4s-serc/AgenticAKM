# ADR-012: Domain-agnostic model abstraction using confidence outputs

**Date**: 2025-10-10
**Status**: Proposed

## Context
The runtime should support different ML tasks and model families without task-specific coupling.

## Decision
Treat models uniformly as variants that emit a prediction confidence metric consumed by the planner and analyzer.

## Consequences
High reusability across tasks. Assumes confidence is well-calibrated and comparable across models; task-specific metrics (e.g., accuracy-at-k, latency constraints) are not natively considered.