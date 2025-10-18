# ADR-011: Synthetic load generation using inter-arrival schedules

**Date**: 2025-10-10
**Status**: Proposed

## Context
Reproducible, controllable workload intensity is needed to stress-test policies.

## Decision
Replay resampled_scaled_inter_arrivals.csv to drive Request_send and emulate varying request rates.

## Consequences
Deterministic experiments and scenario coverage; may not capture real-world burstiness or diurnal patterns; policies may overfit to replayed traces.