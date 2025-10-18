# ADR-006: Scalarization of energy and confidence into a single decision score

**Date**: 2025-10-10
**Status**: Proposed

## Context
The planner needs a unified objective to compare heterogeneous models with differing energy usage and confidence outputs.

## Decision
Combine energy and prediction confidence into a scalar score per model; NAIVE baselines implement simpler fixed-weight heuristics.

## Consequences
Transparent and easy to implement but sensitive to normalization and weighting choices. Omits additional QoS factors (e.g., latency, SLA violations) unless explicitly incorporated.