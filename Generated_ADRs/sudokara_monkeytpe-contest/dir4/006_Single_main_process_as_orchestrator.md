# ADR-006: Single main process as orchestrator

**Date**: 2025-10-14
**Status**: Proposed

## Context
Electron apps centralize lifecycle and window management in the main process.

## Decision
Use the main process (index.js) to manage app lifecycle and create windows for the typing test and leaderboard.

## Consequences
Centralized control of windows and global state, but necessitates strict separation of responsibilities and careful IPC to prevent blocking the main thread or leaking privileged capabilities to renderers.