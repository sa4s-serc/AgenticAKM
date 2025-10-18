# ADR-009: Precompute cluster mappings per model size for fast runtime analysis

**Date**: 2025-10-10
**Status**: Proposed

## Context
Runtime latency budget is tight; cluster inference must be lightweight.

## Decision
Ship Knowledge_get_cluster artifacts that allow O(1) mapping from observed features to cluster/model recommendations.

## Consequences
Very low runtime overhead and deterministic behavior; mappings can become stale with distribution shift; reduces flexibility to adapt without artifact refresh.