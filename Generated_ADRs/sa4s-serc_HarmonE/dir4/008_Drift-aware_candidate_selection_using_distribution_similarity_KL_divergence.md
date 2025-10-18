# ADR-008: Drift-aware candidate selection using distribution similarity (KL divergence)

**Date**: 2025-10-09
**Status**: Proposed

## Context
Selecting a replacement model should consider current data characteristics relative to historical contexts.

## Decision
Analyse computes similarity between recent data distribution and historical drift data (e.g., via KL divergence) to shortlist model versions.

## Consequences
Improves likelihood of picking models suited to current data. Sensitivity to the chosen divergence metric and windowing; may mislead under sparse or noisy drift statistics.