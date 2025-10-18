# ADR-004: Intermediate representation via model.json

**Date**: 2025-10-09
**Status**: Proposed

## Context
Both simulation and visualization need a common system description independent of Python code structure.

## Decision
Emit a model.json from the generator(s) as a stable intermediate representation to drive downstream web visualization and potentially other consumers.

## Consequences
Decouples visualization from code generation; simplifies tooling reuse; requires versioning and schema governance; enables future targets beyond web (e.g., analytics, alternative simulators).