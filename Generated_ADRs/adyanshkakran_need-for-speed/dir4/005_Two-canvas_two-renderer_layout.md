# ADR-005: Two-canvas, two-renderer layout

**Date**: 2025-10-14
**Status**: Proposed

## Context
index.html provides separate containers for the main scene and the mini‑map, and the code configures renderers.

## Decision
Render the main view and mini‑map with separate WebGLRenderer instances bound to different canvases.

## Consequences
Clear separation of views and independent sizing/styling; incurs extra GPU/CPU cost and duplicate state management; more DOM and resize coordination.