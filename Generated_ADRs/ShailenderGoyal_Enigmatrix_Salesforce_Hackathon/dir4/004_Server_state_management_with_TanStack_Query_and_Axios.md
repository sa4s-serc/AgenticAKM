# ADR-004: Server state management with TanStack Query and Axios

**Date**: 2025-10-16
**Status**: Proposed

## Context
The SPA needs resilient data fetching, caching, and synchronization with the API.

## Decision
Use TanStack Query for caching, retries, and cache invalidation, with Axios as the HTTP client.

## Consequences
Improved UX through caching and request deduplication; requires disciplined cache key strategies and error handling patterns; adds an abstraction to learn for contributors.