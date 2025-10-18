# ADR-008: Experiment organization via run naming conventions

**Date**: 2025-10-14
**Status**: Proposed

## Context
Run directories and models encode hyperparameters and assets in names (e.g., 2x256-…, DQN_KO_PEP-…).

## Decision
Encode key configuration details in run and file names rather than centralized metadata.

## Consequences
Human-friendly browsing and quick filtering; brittle and error-prone, hard to query programmatically, and easy to desynchronize from the actual config if scripts change.