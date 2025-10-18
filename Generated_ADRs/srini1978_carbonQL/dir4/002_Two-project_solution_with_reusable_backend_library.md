# ADR-002: Two-project solution with reusable backend library

**Date**: 2025-10-09
**Status**: Proposed

## Context
Solution contains a class library (carbonQLBackend.dll) and a console app (carbonQLConsole) that references it.

## Decision
Separate domain logic into a class library and keep the console as a thin orchestrator.

## Consequences
Promotes reuse and clearer separation of concerns; enables future additional front-ends to consume the same library. Adds minimal build complexity but eases evolution of UI independently of core logic.