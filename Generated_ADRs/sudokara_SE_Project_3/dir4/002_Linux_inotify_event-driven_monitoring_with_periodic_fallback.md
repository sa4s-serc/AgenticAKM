# ADR-002: Linux inotify event-driven monitoring with periodic fallback

**Date**: 2025-10-14
**Status**: Proposed

## Context
Efficiently detecting filesystem changes is critical for timely backups, but cross-platform support is desirable.

## Decision
Use pyinotify (inotify) for event-driven observation on Linux, and provide a polling-based PeriodicStrategy as a portable fallback selectable via configuration.

## Consequences
Low overhead and near-real-time events on Linux; limited portability (macOS/Windows require polling); dual strategy maintenance; potential higher CPU and latency when polling.