# ADR-008: Coexistence of racetrack.js and cartrack.js

**Date**: 2025-10-14
**Status**: Proposed

## Context
Two modules implement similar track generation with minor differences (e.g., guide line rendering).

## Decision
Keep both as alternative/iterative implementations of track construction.

## Consequences
Facilitates experimentation and fallback options; risks code duplication, divergence, and confusion about the authoritative API; complicates maintenance.