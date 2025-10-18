# ADR-003: Vercel for docs hosting

**Date**: 2025-10-13
**Status**: Proposed

## Context
Presence of vercel.json alongside MkDocs configuration.

## Decision
Deploy the generated static site to Vercel.

## Consequences
Pros: quick global CDN, preview deployments per PR, minimal ops. Cons: dependency on a third-party host, Vercel-specific config coupling.