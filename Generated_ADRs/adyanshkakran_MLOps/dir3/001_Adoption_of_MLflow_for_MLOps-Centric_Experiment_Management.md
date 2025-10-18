# ADR-001: Adoption of MLflow for MLOps-Centric Experiment Management

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project required a systematic approach to manage the machine learning lifecycle, ensuring that experiments were trackable, comparable, and reproducible, moving beyond simple, untracked training scripts.

## Decision
MLflow was chosen as the cornerstone of the architecture. The system was designed to meticulously log all experiment runs, capturing hyperparameters, performance metrics, and versioned model artifacts in a structured `mlruns` directory.

## Consequences
This decision resulted in high reproducibility and auditability for every model trained. It streamlined the process of model selection through quantitative comparison and produced self-contained, deployment-ready artifacts, significantly accelerating the path to production. However, it also introduced a dependency on the MLflow ecosystem and its associated tooling.