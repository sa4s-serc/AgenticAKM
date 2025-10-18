# ADR-003: Preload bridge for privileged access

**Date**: 2025-10-14
**Status**: Proposed

## Context
Renderers need limited access to privileged capabilities (e.g., filesystem, IPC) without exposing full Node APIs.

## Decision
Introduce a preload script to expose a constrained API surface from the main process to renderers.

## Consequences
Creates a safer boundary and clearer contract for renderer capabilities, but requires disciplined API design, data validation across IPC, and alignment with Electron security features (e.g., context isolation) to be effective.