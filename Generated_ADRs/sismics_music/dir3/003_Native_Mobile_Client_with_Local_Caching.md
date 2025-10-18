# ADR-003: Native Mobile Client with Local Caching

**Date**: 2025-10-14
**Status**: Proposed

## Context
The Android client needed to provide a fluid and responsive user experience, even when interacting with a large music library over a potentially slow or unreliable network connection.

## Decision
A native Android application was developed, incorporating a local database to cache music metadata (artists, albums, tracks). A Data Access Object (DAO) pattern was used to manage data persistence.

## Consequences
The local cache dramatically improves performance and enables offline browsing capabilities, creating a better user experience. This comes at the cost of increased client-side complexity, as logic must be implemented to manage the cache, handle data synchronization, and deal with potential stale data.