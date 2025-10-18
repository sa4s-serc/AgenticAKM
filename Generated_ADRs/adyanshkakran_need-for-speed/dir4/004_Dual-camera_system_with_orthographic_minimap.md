# ADR-004: Dual-camera system with orthographic mini‑map

**Date**: 2025-10-14
**Status**: Proposed

## Context
Gameplay benefits from both a third‑person racing view and a situational overview.

## Decision
Use a perspective camera for gameplay and an orthographic camera for an overhead mini‑map.

## Consequences
Improves player awareness; adds synchronization work (positions, transforms); increases rendering workload per frame.