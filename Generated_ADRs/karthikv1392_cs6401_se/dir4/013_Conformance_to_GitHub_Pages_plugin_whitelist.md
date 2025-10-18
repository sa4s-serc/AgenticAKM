# ADR-013: Conformance to GitHub Pages plugin whitelist

**Date**: 2025-10-08
**Status**: Proposed

## Context
Only the github-pages gem is declared; no custom Jekyll plugins are used.

## Decision
Stay within the GitHub Pages-supported plugin set and avoid custom plugins.

## Consequences
Ensures compatibility and reliability on GitHub Pages, but restricts advanced Jekyll features, data transformations, and custom generators.