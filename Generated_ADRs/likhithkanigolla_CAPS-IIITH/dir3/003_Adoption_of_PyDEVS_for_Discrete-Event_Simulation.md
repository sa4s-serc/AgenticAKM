# ADR-003: Adoption of PyDEVS for Discrete-Event Simulation

**Date**: 2025-10-09
**Status**: Proposed

## Context
The project required an executable target to run the generated system models. A formal simulation framework was necessary to handle core concepts of discrete-event systems, such as event scheduling, state transitions, and component interaction, without having to build this complex infrastructure from scratch.

## Decision
The PyDEVS framework was selected as the specific technological target for code generation. The entire system is architected to produce Python code that conforms to the PyDEVS API for atomic and coupled models, making the output directly executable by the PyDEVS simulation engine.

## Consequences
This choice leverages a powerful, existing library, providing a standardized and robust execution environment for the simulations, which accelerates development. However, it tightly couples the code generation logic to the PyDEVS paradigm, making it difficult to retarget a different simulation framework in the future without significant rework.