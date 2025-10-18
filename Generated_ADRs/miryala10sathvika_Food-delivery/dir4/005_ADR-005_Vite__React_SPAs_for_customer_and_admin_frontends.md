# ADR-005: ADR-005: Vite + React SPAs for customer and admin frontends

**Date**: 2025-10-13
**Status**: Proposed

## Context
Both frontend and admin are Vite-powered React applications with separate configs and assets.

## Decision
Keep two separate React SPAs built with Vite, one for customers and one for admins. No SSR at this stage. Each app builds and deploys independently.

## Consequences
- Fast local dev and modern bundling defaults.
- Clear separation of user-facing and operational surfaces.
- Duplicate configuration between apps; potential later introduction of a shared UI library if overlap grows.
- Each app must configure its own environment variables (VITE_*).