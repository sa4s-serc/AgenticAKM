# ADR-012: Rely solely on GitHub Pages for builds (no external CI)

**Date**: 2025-10-08
**Status**: Proposed

## Context
No CI configuration is indicated; builds are implied to occur via GitHub Pages.

## Decision
Depend on GitHub Pages as the primary and only build/publish pipeline.

## Consequences
Low operational burden but limits pre-deploy validation, link checking, and custom build steps; makes builds subject to GitHub Pages constraints and timing.