# ADR-010: Separate static asset pipelines for backend and frontend

**Date**: 2025-10-14
**Status**: Proposed

## Context
Backend serves static files from public/ (including stylesheets and images), while the frontend has its own assets and build pipeline.

## Decision
Maintain distinct static asset flows: backend static for server-rendered pages and frontend build artifacts served via Nginx.

## Consequences
Allows backend-rendered pages to operate independently and optimizes delivery of SPA assets; increases operational complexity, risks duplication or inconsistency, and requires coordinated caching/versioning strategies.