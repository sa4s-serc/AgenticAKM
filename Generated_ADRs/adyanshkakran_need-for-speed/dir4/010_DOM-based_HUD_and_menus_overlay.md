# ADR-010: DOM-based HUD and menus overlay

**Date**: 2025-10-14
**Status**: Proposed

## Context
UI elements like timers, health, fuel, and instructions are rendered in HTML/CSS.

## Decision
Implement all HUD/menus in the DOM on top of the WebGL canvases.

## Consequences
Rapid iteration and accessibility of web UI; decouples UI from 3D rendering; requires careful synchronization and can incur layout/paint costs on frequent updates.