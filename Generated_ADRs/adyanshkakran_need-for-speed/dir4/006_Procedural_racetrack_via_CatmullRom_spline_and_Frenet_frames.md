# ADR-006: Procedural racetrack via Catmull–Rom spline and Frenet frames

**Date**: 2025-10-14
**Status**: Proposed

## Context
The track must be generated from control points with smooth curvature and consistent width.

## Decision
Compute tangents, normals, and binormals along a Catmull–Rom path to extrude a road surface.

## Consequences
Enables flexible, parametric track layouts and predictable AI paths; requires careful math for continuity and banking; debugging is more complex than using prebuilt meshes.