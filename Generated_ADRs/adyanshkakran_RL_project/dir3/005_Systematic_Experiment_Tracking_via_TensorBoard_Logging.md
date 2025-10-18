# ADR-005: Systematic Experiment Tracking via TensorBoard Logging

**Date**: 2025-10-14
**Status**: Proposed

## Context
Training RL agents is an iterative process that generates a large volume of metrics (e.g., reward, loss, episode length). To analyze performance, compare runs, and debug models effectively, this data must be systematically captured and stored.

## Decision
To integrate TensorBoard logging as a core component of the experimentation workflow. A dedicated `logs/` directory is used to store event files from training runs, with a structured naming convention that captures agent type and hyperparameters.

## Consequences
This is a best-practice decision that significantly enhances the project's research capabilities. It enables deep, visual analysis of agent behavior and performance, improving reproducibility and making the experimental results more credible and easier to interpret. It moves the project from simple scripting towards a more robust MLOps-oriented workflow.