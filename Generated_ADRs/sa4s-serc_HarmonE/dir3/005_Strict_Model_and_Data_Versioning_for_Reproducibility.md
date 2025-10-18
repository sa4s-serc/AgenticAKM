# ADR-005: Strict Model and Data Versioning for Reproducibility

**Date**: 2025-10-09
**Status**: Proposed

## Context
To enable reliable model switching and analysis (e.g., using KL-divergence), it is essential to have a complete and trustworthy record of each model's provenance, including the exact data it was trained on.

## Decision
A strict versioning discipline was enforced where each model artifact is packaged and stored directly with the dataset used to train it. This creates a self-contained, reproducible unit managed by the `train_models.py` and `retrain.py` scripts.

## Consequences
This decision guarantees full reproducibility, which is critical for auditing, debugging, and enabling reliable rollbacks. It also provides the necessary historical data distributions for the 'Analyze' phase to make informed decisions. The primary negative consequence is a significant increase in storage requirements, as training data is duplicated for each model version.