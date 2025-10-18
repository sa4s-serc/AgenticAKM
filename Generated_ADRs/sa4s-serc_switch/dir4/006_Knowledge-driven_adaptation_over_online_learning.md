# ADR-006: Knowledge-driven adaptation over online learning

**Date**: 2025-10-10
**Status**: Proposed

## Context
The research prototype prioritizes stability, interpretability, and repeatability over continuous model updates.

## Decision
Base adaptation on a static Knowledge base and rule/cluster logic instead of live online learning.

## Consequences
Predictable and explainable behavior with fewer moving parts; simpler to validate; slower to adapt to concept drift and may need manual updates to maintain effectiveness.