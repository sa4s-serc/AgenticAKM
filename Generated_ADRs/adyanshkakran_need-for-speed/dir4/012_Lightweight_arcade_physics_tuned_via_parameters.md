# ADR-012: Lightweight arcade physics tuned via parameters

**Date**: 2025-10-14
**Status**: Proposed

## Context
Gameplay parameters (handling, friction, max speed, laps) are set directly in code.

## Decision
Avoid full physics engines; implement simplified kinematics with manual tuning.

## Consequences
Predictable, performant controls suitable for arcade feel; limited realism and collision fidelity; heavy reliance on hand tuning for fun and stability.