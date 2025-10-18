# ADR-009: Reproducible benchmarking and Ray-powered capacity search

**Date**: 2025-10-14
**Status**: Proposed

## Context
Operators need to explore throughput/latency trade-offs and identify optimal configurations under realistic traffic patterns.

## Decision
Provide a benchmark harness with synthetic and trace-driven request generators and a Ray-driven capacity search framework to explore regime space programmatically.

## Consequences
Enables systematic, repeatable performance studies and automated search; requires Ray in the benchmarking environment and careful interpretation of synthetic vs. production traffic fidelity.