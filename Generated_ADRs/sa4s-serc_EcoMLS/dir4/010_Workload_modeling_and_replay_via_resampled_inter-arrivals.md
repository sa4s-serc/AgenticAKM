# ADR-010: Workload modeling and replay via resampled inter-arrivals

**Date**: 2025-10-10
**Status**: Proposed

## Context
Evaluation should reflect realistic request dynamics while remaining reproducible for controlled experiments.

## Decision
Generate and replay requests using resampled, scaled inter-arrival distributions (resampled_scaled_inter_arrivals.csv) in Request_send.py.

## Consequences
Improves repeatability and enables stress tests. May not capture real-world burstiness, seasonality, or multi-tenant interference without further extensions.