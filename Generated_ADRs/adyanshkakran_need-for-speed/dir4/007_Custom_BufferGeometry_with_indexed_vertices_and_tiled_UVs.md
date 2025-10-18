# ADR-007: Custom BufferGeometry with indexed vertices and tiled UVs

**Date**: 2025-10-14
**Status**: Proposed

## Context
The road needs repeating textures (e.g., markings) and efficient GPU usage.

## Decision
Build an indexed BufferGeometry for the track with UVs that tile, and use multi‑material strips for markings.

## Consequences
Achieves crisp, repeated details and lower memory via indexed buffers; increases implementation complexity; multiple materials can raise draw calls.