# ADR-014: Inclusion of OrbitControls and Stats.js in runtime

**Date**: 2025-10-14
**Status**: Proposed

## Context
Development tools for camera inspection and performance monitoring are initialized with the scene.

## Decision
Ship with OrbitControls and a performance stats overlay enabled in the app.

## Consequences
Aids debugging and tuning; potential user input conflicts and small runtime overhead; should be gated by environment flags for production builds.