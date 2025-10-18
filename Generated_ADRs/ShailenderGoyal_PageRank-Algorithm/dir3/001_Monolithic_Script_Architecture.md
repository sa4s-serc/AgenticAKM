# ADR-001: Monolithic Script Architecture

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project is designed as a focused, self-contained utility or educational tool with a singular purpose: implementing and visualizing the PageRank algorithm.

## Decision
All application logic, including the core PageRank computation, network visualization, convergence plotting, and result output, was consolidated into a single executable script (`project.py`).

## Consequences
This minimalistic approach enhances simplicity and portability, making the project easy to understand and execute without a complex setup. However, it results in tight coupling between computation and presentation, which hinders modular testing, code reusability, and the ability to scale or extend the application for more complex use cases.