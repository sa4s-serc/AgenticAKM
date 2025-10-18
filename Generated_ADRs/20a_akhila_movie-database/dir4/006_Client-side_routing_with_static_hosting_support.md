# ADR-006: Client-side routing with static hosting support

**Date**: 2025-10-10
**Status**: Proposed

## Context
Routes cover Home, Movie, and NotFound; a public/_redirects file is present.

## Decision
Use react-router-dom for navigation and configure a fallback redirect for unknown paths on static hosts.

## Consequences
Seamless SPA navigation and deep-linking on static deployments; no server-side rendering or pre-rendering for SEO-sensitive routes; initial navigation incurs bundle download cost.