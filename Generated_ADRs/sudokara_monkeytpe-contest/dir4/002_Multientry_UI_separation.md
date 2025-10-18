# ADR-002: Multi‑entry UI separation

**Date**: 2025-10-14
**Status**: Proposed

## Context
Typing test and leaderboard are distinct user flows.

## Decision
Use separate HTML entry points and renderer scripts (index.html/renderer.js and leaderboard.html/leaderboard.js), potentially as separate windows.

## Consequences
Improves separation of concerns and simplifies per‑view logic, but introduces state sharing/synchronization challenges and higher resource usage from multiple renderer processes.