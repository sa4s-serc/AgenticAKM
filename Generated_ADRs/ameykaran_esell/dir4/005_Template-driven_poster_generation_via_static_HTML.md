# ADR-005: Template-driven poster generation via static HTML

**Date**: 2025-10-14
**Status**: Proposed

## Context
Poster generation uses a base HTML template (backend/poster.html) and writes out concrete posters to backend/posters/.

## Decision
Generate posters by injecting LLM-derived content into static HTML templates.

## Consequences
Pros: predictable rendering, fast generation, easy theming via template edits. Cons: limited runtime interactivity; harder to personalize per viewer; scaling to multiple themes requires template management.