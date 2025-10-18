# ADR-013: Reuse of spline path for AI and pickup placement

**Date**: 2025-10-14
**Status**: Proposed

## Context
Opponent pathing and fuel can placement derive from the same track reference.

## Decision
Spawn AI opponents and fuel pickups along the computed track path.

## Consequences
Keeps logic consistent and simplifies placement; yields predictable pickup locations; may reduce gameplay variety and challenge without additional randomization.