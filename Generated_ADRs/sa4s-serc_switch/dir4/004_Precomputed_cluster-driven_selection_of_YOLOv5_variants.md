# ADR-004: Precomputed cluster-driven selection of YOLOv5 variants

**Date**: 2025-10-10
**Status**: Proposed

## Context
Runtime must select among YOLOv5 n/s/m/l/x models to meet performance/accuracy trade-offs under varying workload characteristics.

## Decision
Use precomputed cluster mappings in the Knowledge base to guide Analyzer/Planner decisions for model variant selection.

## Consequences
Enables fast, deterministic runtime choices; reduces compute overhead of decision-making; requires upkeep of mappings and retraining when data shifts; may underperform on unseen distributions.