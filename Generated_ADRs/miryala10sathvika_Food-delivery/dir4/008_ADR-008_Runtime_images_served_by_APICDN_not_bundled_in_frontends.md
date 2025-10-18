# ADR-008: ADR-008: Runtime images served by API/CDN, not bundled in frontends

**Date**: 2025-10-13
**Status**: Proposed

## Context
frontend/src/assets/assets.js centralizes static UI assets and also provides mock data. Runtime food images appear in backend/uploads.

## Decision
Bundle only static UI assets with frontends. Runtime content (uploaded food images) must be referenced via URLs returned by the backend or CDN. Frontend components should consume imageUrl fields from API responses instead of importing uploaded files.

## Consequences
- Smaller bundles and fewer accidental rebuilds.
- Clear separation of static assets vs. runtime content.
- API must include image URLs; caching and invalidation are handled at the CDN where applicable.