# ADR-012: Android app with DAO-based SQLite, event-driven UI, and legacy libraries

**Date**: 2025-10-14
**Status**: Proposed

## Context
Android module uses Activities, Db.java DAOs, event objects, adapters, DragSortListView, and a local android-query jar.

## Decision
Implement the Android client with a custom DAO layer and event-based communication, incorporating third-party UI and vendored jar dependencies.

## Consequences
Works on older Android APIs and avoids heavier frameworks; harder testing and lifecycle management versus Jetpack components; vendored jars complicate updates and security fixes; potential Play Store policy friction for outdated libs.