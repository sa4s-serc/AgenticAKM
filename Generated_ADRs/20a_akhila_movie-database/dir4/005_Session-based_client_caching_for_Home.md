# ADR-005: Session-based client caching for Home

**Date**: 2025-10-10
**Status**: Proposed

## Context
Home state is restored/persisted via sessionStorage to avoid refetching.

## Decision
Persist the Home view’s list/search state to sessionStorage and restore it on revisit.

## Consequences
Faster perceived performance and fewer API calls; cache is per-tab and ephemeral, can become stale, and lacks explicit invalidation policies.