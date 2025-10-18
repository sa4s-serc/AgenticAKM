# ADR-002: Multi-Algorithm Architecture for Comparative Analysis

**Date**: 2025-10-14
**Status**: Proposed

## Context
Video temporal puzzle solving is a complex research problem with no single definitive solution. Different strategies, such as greedy searches, hierarchical methods, or machine learning, offer different trade-offs in terms of accuracy, speed, and complexity.

## Decision
Instead of a single solver, the project was structured as a testbed with multiple, independent, and interchangeable reconstruction algorithms (`algorithm1.py` through `algorithm5.py`). Each script implements a distinct strategy to solve the same problem.

## Consequences
This architecture is highly extensible and ideal for research, as it allows for easy addition, testing, and side-by-side comparison of new methods. It modularizes the core logic, isolating each approach. A potential drawback is the risk of code duplication for common tasks (like data loading) if not managed with shared utilities.