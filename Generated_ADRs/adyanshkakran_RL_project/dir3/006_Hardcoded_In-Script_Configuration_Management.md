# ADR-006: Hardcoded In-Script Configuration Management

**Date**: 2025-10-14
**Status**: Proposed

## Context
For a research-focused project, the primary goal is often to get experiments running quickly. Implementing a formal configuration system can feel like premature optimization during the initial development and exploration phase.

## Decision
To hardcode critical hyperparameters—such as network architecture (e.g., `2x256`), learning rates, and dataset choices—directly within the training scripts themselves.

## Consequences
This approach is simple and allows for very fast initial iteration. However, it severely damages long-term maintainability and reproducibility. Running new experiments or performing hyperparameter sweeps requires manual code changes, which is inefficient, error-prone, and makes it difficult to track the exact configuration used for a given result.