# ADR-010: Switch models at request granularity via an Execute module

**Date**: 2025-10-10
**Status**: Proposed

## Context
Workload and scene complexity fluctuate per-request, requiring rapid adaptation.

## Decision
Evaluate the selected policy each inference and switch the active YOLOv5 variant when indicated.

## Consequences
High responsiveness to changing conditions and improved aggregate utility; potential switching overhead, cache misses, and cold starts must be managed to avoid thrashing.