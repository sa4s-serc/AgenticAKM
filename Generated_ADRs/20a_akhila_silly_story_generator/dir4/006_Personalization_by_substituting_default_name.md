# ADR-006: Personalization by substituting default name

**Date**: 2025-10-10
**Status**: Proposed

## Context
Allow the user to personalize the story output.

## Decision
If a custom name is provided, replace occurrences of the default name Bob in the generated story.

## Consequences
Straightforward UX; must handle empty/whitespace input and ensure correct scoping of replacements (avoid partial-word matches); input sanitization needed to prevent injection if inserted as HTML.