# ADR-003: Dual-domain experimentation strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
Saved models include SAC_Hopper-v4 while logs reference KO/PEP/IBM/WBA experiments.

## Decision
Support both finance-specific portfolio tasks and standard control benchmarks within one workspace.

## Consequences
Improves generality testing and comparative baselines; increases setup and data handling complexity; raises need for environment-agnostic abstractions that the current per-script design may not fully provide.