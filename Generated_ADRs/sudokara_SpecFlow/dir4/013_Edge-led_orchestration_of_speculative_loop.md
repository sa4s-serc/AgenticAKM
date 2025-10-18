# ADR-013: Edge-led orchestration of speculative loop

**Date**: 2025-10-14
**Status**: Proposed

## Context
Minimizing round-trips and maintaining prompt state at the edge can improve latency.

## Decision
Have the edge client orchestrate draft-token generation and manage communication cycles with the cloud server, including connection reuse.

## Consequences
Reduces per-token overhead and centralizes state at the edge; requires robust error handling, reconnection strategies, and backpressure to handle network variability.