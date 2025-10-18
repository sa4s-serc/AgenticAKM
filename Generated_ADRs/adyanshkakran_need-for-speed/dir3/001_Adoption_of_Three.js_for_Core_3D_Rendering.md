# ADR-001: Adoption of Three.js for Core 3D Rendering

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project's primary requirement was to build an interactive 3D car racing game that runs natively in a web browser without plugins. A powerful, high-level, and well-supported library was needed to handle the complexities of WebGL, including scene management, rendering, and asset loading.

## Decision
The project was built fundamentally on Three.js. This library was chosen to manage all aspects of 3D rendering, from setting up the scene, cameras, and lighting to loading and displaying 3D models.

## Consequences
This decision enables the creation of a rich, hardware-accelerated 3D experience directly in the browser. It leverages a mature ecosystem with extensive documentation and community support. The application's performance is, however, dependent on the client's hardware and browser's WebGL implementation.