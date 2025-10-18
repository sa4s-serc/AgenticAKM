# ADR-007: Instrument specific telemetry fields for feedback control

**Date**: 2025-10-10
**Status**: Proposed

## Context
The controller needs timely, informative signals to detect context and performance shortfalls.

## Decision
Log per-inference average confidence, response time, CPU usage, and number of boxes to monitor.csv.

## Consequences
Sufficient features for clustering and utility estimation; missing GPU/memory I/O metrics limits applicability to GPU-heavy deployments; CSV logging adds I/O overhead.