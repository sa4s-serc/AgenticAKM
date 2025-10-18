# ADR-006: Kullback-Leibler (KL) Divergence for Model Candidate Selection

**Date**: 2025-10-09
**Status**: Proposed

## Context
During the 'Analyze' phase, the system needs a principled, data-driven method to select the best replacement model from the available pool when data drift is suspected.

## Decision
Kullback-Leibler (KL) divergence was chosen as the statistical method to compare the distribution of the current inference data against the historical training data distribution of each versioned model. The model with the lowest KL divergence is selected as the best candidate.

## Consequences
This provides a robust and automated method for model selection that is more sophisticated than relying on simple performance metric thresholds. It proactively identifies a model that is statistically most similar to the current data regime. The downside is that calculating KL divergence can be computationally intensive and its effectiveness assumes that a smaller distributional shift directly correlates with better model performance.