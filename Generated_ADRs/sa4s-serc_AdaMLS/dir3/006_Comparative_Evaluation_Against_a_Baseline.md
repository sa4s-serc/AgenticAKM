# ADR-006: Comparative Evaluation Against a Baseline

**Date**: 2025-10-10
**Status**: Proposed

## Context
To scientifically validate the benefits of the complex adaptive strategy (AdaMLS), its performance needed to be rigorously compared against simpler, alternative approaches.

## Decision
A dedicated baseline system, named `NAVIE`, was developed alongside AdaMLS. Experiments were designed to compare the performance of AdaMLS against both `NAVIE` and static configurations (i.e., always using a single model size). Dedicated notebooks were created to plot these comparative results.

## Consequences
This approach provides a robust, quantitative validation of the adaptive system's effectiveness, which is critical for a research project. The results clearly demonstrate the value added by the adaptive logic. The downside is the significant increase in development and experimentation effort required to build and test multiple systems.