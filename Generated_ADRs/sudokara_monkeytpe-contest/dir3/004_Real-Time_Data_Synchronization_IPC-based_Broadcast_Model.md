# ADR-004: Real-Time Data Synchronization: IPC-based Broadcast Model

**Date**: 2025-10-14
**Status**: Proposed

## Context
When a new score is submitted, all open application windows, especially the leaderboard window, must update in real-time to reflect the new state without requiring a manual refresh.

## Decision
An event-driven model using Electron's IPC was implemented. After the Main process persists a new score to `leaderboard.json`, it broadcasts the entire updated and sorted leaderboard to all active Renderer processes. Listening windows then re-render their display with the new data.

## Consequences
This provides a seamless and responsive real-time experience for users. It effectively decouples the data source (Main process) from the UI (Renderer processes). The primary downside is inefficiency at scale; broadcasting the full dataset on every update is viable for a small leaderboard but would be a performance bottleneck with a very large number of entries.