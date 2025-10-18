# ADR-005: Physical Separation of Code, Data, and Experiment Artifacts

**Date**: 2025-10-14
**Status**: Proposed

## Context
Following software engineering best practices, the project needed to manage different asset types—source code, datasets, and generated outputs—in a clean and isolated manner to improve version control and maintainability.

## Decision
A distinct directory structure was enforced, isolating source code (`linear_regression/`), raw datasets (`data/`), and experiment results (`mlruns/`).

## Consequences
This separation keeps the version control history clean by not tracking large data files or voluminous experiment logs. It provides a clear and navigable project layout, making it easier for new developers to understand. It also facilitates independent management and storage strategies for each asset type (e.g., code in Git, data in a data lake).