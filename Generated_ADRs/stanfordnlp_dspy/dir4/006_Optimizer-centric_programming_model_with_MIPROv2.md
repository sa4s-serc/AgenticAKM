# ADR-006: Optimizer-centric programming model with MIPROv2

**Date**: 2025-10-13
**Status**: Proposed

## Context
Optimizers include MIPROv2, KNN variants, Bootstrap methods, Ensemble, SIMBA, COPRO, and GEPA docs.

## Decision
Make optimizers first-class for program synthesis/tuning and comparative evaluation.

## Consequences
Pros: systematic improvement workflows, supports research and A/B testing. Cons: requires consistent interfaces and evaluation harnesses; users need to understand optimizer assumptions.