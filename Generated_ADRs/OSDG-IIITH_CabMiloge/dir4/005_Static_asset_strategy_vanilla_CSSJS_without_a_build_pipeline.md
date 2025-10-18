# ADR-005: Static asset strategy: vanilla CSS/JS without a build pipeline

**Date**: 2025-10-14
**Status**: Proposed

## Context
Static assets are plain CSS and JS files served with templates; no bundler config is present.

## Decision
Serve unbundled static assets directly from Flask/static with no frontend build step.

## Consequences
- Minimal tooling and fast builds; straightforward local development
- Misses minification, tree-shaking, and code splitting; suboptimal load performance at scale
- Cache/versioning must be handled via filename hashing or response headers
- Easier to maintain for small to medium sites without complex frontend needs