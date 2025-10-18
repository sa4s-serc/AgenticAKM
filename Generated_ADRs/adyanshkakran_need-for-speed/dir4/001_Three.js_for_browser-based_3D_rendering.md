# ADR-001: Three.js for browser-based 3D rendering

**Date**: 2025-10-14
**Status**: Proposed

## Context
The app is a web racing experience that needs real-time 3D graphics in the browser.

## Decision
Adopt Three.js as the core 3D engine for scene, cameras, lighting, materials, loaders, and controls.

## Consequences
Enables cross‑platform, plugin‑free 3D with a large ecosystem; places physics, collision, and game-loop responsibilities on the app; performance depends on careful scene and asset management.