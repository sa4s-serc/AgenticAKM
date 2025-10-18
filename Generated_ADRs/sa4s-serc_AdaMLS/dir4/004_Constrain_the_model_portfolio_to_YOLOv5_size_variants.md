# ADR-004: Constrain the model portfolio to YOLOv5 size variants

**Date**: 2025-10-10
**Status**: Proposed

## Context
Need a set of models with consistent APIs but different accuracy–latency trade-offs.

## Decision
Target YOLOv5 nano, small, medium, large, and xlarge as switchable options.

## Consequences
Predictable performance scaling and simplified switching; excludes newer architectures; portability is high but limits the search space to a single family.