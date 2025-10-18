# ADR-009: Pluggable baseline strategies and static-model baselines

**Date**: 2025-10-10
**Status**: Proposed

## Context
Demonstrating the value of adaptation requires comparisons against simpler heuristics and fixed model choices.

## Decision
Implement NAIVE1–3 planners with alternative scoring heuristics and include static non-switching models as bounds.

## Consequences
Enables credible, reproducible comparisons and ablation studies. Adds maintenance overhead and potential configuration drift across strategies.