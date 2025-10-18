# ADR-003: DEVS-style generation without strict PyDEVS coupling

**Date**: 2025-10-09
**Status**: Proposed

## Context
Simulation semantics are DEVS-like, but strict adherence to a specific engine may constrain portability and evolution.

## Decision
Generate DEVS-style Python classes with PyDEVS-like patterns while treating internal semantics (e.g., time-advance) as implementation-specific unless confirmed.

## Consequences
Increases flexibility and reduces external dependency lock-in; risks semantic drift from standard DEVS behavior; may complicate interoperability with established DEVS engines.