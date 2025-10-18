# ADR-004: Pluggable Architecture for Experimental Algorithms

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project's goal is not just to create a single object detection app, but to serve as a research platform for evaluating different adaptive scheduling strategies. A monolithic design would make it difficult to compare and contrast various decision-making algorithms.

## Decision
The architecture was designed to be a testbed by implementing the core logic in interchangeable components. The presence of multiple `CameraFragment` implementations (`naive`, `epsilon`, `mlfq`) indicates a strategy pattern, allowing different scheduling algorithms to be plugged in and tested with minimal changes to the surrounding codebase.

## Consequences
This makes the project highly extensible and ideal for research and experimentation. New strategies can be added easily, facilitating comparative analysis. However, it may imply that the code is not fully optimized for a single, production-hardened use case, but rather for flexibility and evaluation.