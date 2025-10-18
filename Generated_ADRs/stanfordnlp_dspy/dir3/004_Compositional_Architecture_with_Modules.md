# ADR-004: Compositional Architecture with 'Modules'

**Date**: 2025-10-13
**Status**: Proposed

## Context
LLM-based applications frequently use recurring reasoning patterns, such as chain-of-thought, tool use (ReAct), or simple prediction. Building these from scratch for every application is inefficient.

## Decision
Provide a library of pre-built, composable 'Module' classes (e.g., `Predict`, `ChainOfThought`, `ReAct`). Developers construct complex applications by assembling and composing these modules, similar to building a neural network in PyTorch.

## Consequences
This design promotes code reuse, modularity, and a clear separation of concerns. It allows developers to build sophisticated reasoning pipelines from simple, well-tested components, accelerating development and making programs easier to understand and debug.