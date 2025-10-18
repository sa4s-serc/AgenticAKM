# ADR-006: Client-Side Caching for Performance Optimization

**Date**: 2025-10-10
**Status**: Proposed

## Context
To improve the perceived performance and user experience on subsequent visits or page reloads within a single session, a strategy was needed to avoid redundant fetching of the application's initial data.

## Decision
The `useHomeFetch` hook implements a client-side caching mechanism using the browser's `sessionStorage`. The initial API response for the home page is stored and then retrieved from this cache on subsequent loads within the same session.

## Consequences
This significantly speeds up initial load times for returning users and reduces API call volume. The trade-off is that the cached data can become stale if the source data changes frequently. The benefits are also limited to a single browser session, as `sessionStorage` is cleared upon closing the tab.