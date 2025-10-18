# ADR-008: Search and pagination via incremental fetch and Load More

**Date**: 2025-10-10
**Status**: Proposed

## Context
Home view supports searching and appending paginated results with a Load more control.

## Decision
Implement client-controlled pagination that appends results rather than infinite scrolling.

## Consequences
Simple UX and implementation with clear user intent; more user interaction required versus infinite scroll and more complex to preserve pagination state in URLs.