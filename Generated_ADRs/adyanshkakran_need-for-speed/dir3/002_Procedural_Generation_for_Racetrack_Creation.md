# ADR-002: Procedural Generation for Racetrack Creation

**Date**: 2025-10-14
**Status**: Proposed

## Context
A key challenge was creating a detailed and customizable racetrack. Relying on static, pre-modeled 3D assets for the track would increase file size, limit variability, and make design iterations slow and cumbersome.

## Decision
To programmatically generate the racetrack's geometry at runtime. The architecture uses `CatmullRomCurve3` to define a smooth path and then constructs custom `BufferGeometry` along that curve, including vertices and UV coordinates for texturing.

## Consequences
This approach significantly reduces the initial asset download size and provides immense flexibility for modifying or even randomizing the track layout with minimal code changes. The trade-off is an increase in computational complexity within the application code and a performance cost during the initial track generation phase.