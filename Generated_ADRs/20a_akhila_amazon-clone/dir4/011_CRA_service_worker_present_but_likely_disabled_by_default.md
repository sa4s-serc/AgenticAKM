# ADR-011: CRA service worker present but likely disabled by default

**Date**: 2025-10-10
**Status**: Proposed

## Context
serviceWorker.js is included as part of CRA’s scaffold.

## Decision
Keep the default CRA service worker setup (typically not registered) unless explicitly enabled.

## Consequences
Avoids offline caching pitfalls and stale content issues; forfeits PWA benefits like offline support and asset caching; enabling later requires explicit cache versioning and update strategies.