# ADR-006: Provide a baseline (NAVIE) with mirrored structure and simpler logic

**Date**: 2025-10-10
**Status**: Proposed

## Context
Scientific evaluation needs a comparator to quantify the benefit of adaptive switching.

## Decision
Implement NAVIE as a separate runtime stack with heuristic or static mappings encoded in knowledge.csv.

## Consequences
Enables A/B comparisons and ablation studies; duplicate structure increases maintenance; risk of code drift between stacks.