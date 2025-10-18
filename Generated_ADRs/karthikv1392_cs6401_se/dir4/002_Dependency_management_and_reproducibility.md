# ADR-002: Dependency management and reproducibility

**Date**: 2025-10-08
**Status**: Proposed

## Context
Gemfile includes github-pages and webrick, and Gemfile.lock is committed.

## Decision
Pin dependencies using the github-pages gem and lock versions with Gemfile.lock; use webrick for local development server.

## Consequences
Reproducible builds aligned with GitHub Pages environment; upgrades are gated by github-pages releases, potentially lagging upstream Jekyll features; contributors must use compatible Ruby versions.