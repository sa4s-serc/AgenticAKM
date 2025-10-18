# ADR-009: SPA-compatible hosting and navigation fallback

**Date**: 2025-10-14
**Status**: Proposed

## Context
A public/_redirects file is present and an Nginx layer is used to serve the SPA.

## Decision
Configure the web server to redirect unknown paths to the SPA entry point so client-side routing works with deep links and refreshes.

## Consequences
Prevents 404s on client routes and enables seamless navigation; requires careful exclusion of API paths from the fallback, and misconfiguration can mask genuine server-side errors.