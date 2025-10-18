# ADR-011: GLTF/GLB assets served from public/ via Vite static hosting

**Date**: 2025-10-14
**Status**: Proposed

## Context
Cars, environment, and props are stored as GLTF/GLB with textures in public/.

## Decision
Load runtime assets directly from the static public/ folder without a custom pipeline.

## Consequences
Simple development and deployment; larger network payloads and runtime parse costs; fewer opportunities for compression/optimization than a bespoke asset pipeline.