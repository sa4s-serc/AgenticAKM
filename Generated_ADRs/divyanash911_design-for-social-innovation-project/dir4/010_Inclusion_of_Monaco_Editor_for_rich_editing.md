# ADR-010: Inclusion of Monaco Editor for rich editing

**Date**: 2025-10-13
**Status**: Proposed

## Context
The lockfile references the Monaco editor alongside content authoring components.

## Decision
Integrate Monaco Editor to support advanced editing experiences for content authoring.

## Consequences
Enhances authoring capabilities but increases bundle size and loading time; demands lazy-loading and code-splitting strategies to preserve performance.