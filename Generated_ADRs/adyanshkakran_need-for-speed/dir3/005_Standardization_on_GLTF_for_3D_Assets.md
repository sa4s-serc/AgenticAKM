# ADR-005: Standardization on GLTF for 3D Assets

**Date**: 2025-10-14
**Status**: Proposed

## Context
The game needed to load multiple complex 3D models for cars, the stadium, and other objects. An efficient, web-optimized 3D asset format was essential to ensure fast loading times and good rendering performance.

## Decision
The GLTF (.gltf, .glb) format was chosen as the standard for all 3D assets in the project. This includes the car models and the surrounding environment.

## Consequences
Using GLTF, which is often called the 'JPEG of 3D', ensures efficient transmission and fast parsing of 3D models, which is critical for web performance. This choice aligns perfectly with the Three.js ecosystem, which has robust and well-maintained GLTF loaders. It mandates that all 3D modeling work must be exported to this specific format.