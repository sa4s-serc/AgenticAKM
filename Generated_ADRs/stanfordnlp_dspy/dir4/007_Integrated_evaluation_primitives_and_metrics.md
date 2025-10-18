# ADR-007: Integrated evaluation primitives and metrics

**Date**: 2025-10-13
**Status**: Proposed

## Context
Evaluation includes Evaluate, EvaluationResult, CompleteAndGrounded, SemanticF1, and exact/passage match.

## Decision
Ship evaluation as part of the public API to encourage measurable development.

## Consequences
Pros: standardized metrics and processes, reproducible comparisons, easier CI integration. Cons: metric selection may bias development; upkeep required as tasks diversify.