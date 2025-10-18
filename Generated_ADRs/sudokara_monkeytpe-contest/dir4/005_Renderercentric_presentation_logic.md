# ADR-005: Renderer‑centric presentation logic

**Date**: 2025-10-14
**Status**: Proposed

## Context
The UI is implemented with web technologies and split by feature.

## Decision
Place feature‑specific logic in dedicated renderer scripts (renderer.js for typing test, leaderboard.js for leaderboard).

## Consequences
Keeps code organized per view and reduces coupling, but can lead to duplicated utilities and requires explicit patterns for sharing common modules across renderers.