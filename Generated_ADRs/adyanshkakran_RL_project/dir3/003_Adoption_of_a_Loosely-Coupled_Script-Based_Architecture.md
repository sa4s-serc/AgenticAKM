# ADR-003: Adoption of a Loosely-Coupled, Script-Based Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project was conceived as an experimental framework for research and comparison of RL algorithms, not as a monolithic, production-grade application. The focus was on flexibility and the ability to run and iterate on individual components independently.

## Decision
The system was architected as a collection of separate, standalone Python scripts. Each major algorithm (e.g., `DDPG.py`, `SAC.py`) has its own script for training, with other scripts dedicated to evaluation (`test.py`) or visualization (`plot.py`). There is no single, unified entry point.

## Consequences
This modular structure is highly effective for rapid prototyping and isolated experimentation. However, it leads to a lack of a unified interface, making it difficult to orchestrate complex experiments programmatically. It can also result in code duplication for shared functionalities like data loading or model evaluation across different scripts.