# ADR-010: Environment configuration and static deployment posture

**Date**: 2025-10-10
**Status**: Proposed

## Context
.env is used for runtime configuration; public/_redirects and manifest/icons hint at static hosting (e.g., Netlify).

## Decision
Store API configuration in environment variables at build time and deploy as a static SPA with redirects configured.

## Consequences
Straightforward environment management and simple deployment; public API keys are exposed to clients, subject to rate limits and potential misuse, and the app depends on CORS and third-party API availability.