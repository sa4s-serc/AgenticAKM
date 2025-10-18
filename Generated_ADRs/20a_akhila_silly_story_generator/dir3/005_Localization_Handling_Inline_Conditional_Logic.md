# ADR-005: Localization Handling: Inline Conditional Logic

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application required a feature to adapt the story's content (specifically, units of measurement) based on the user's selection of a region (US or UK).

## Decision
To implement the localization logic as a simple conditional (if/else) block within the main JavaScript function. This block checks the selected region and applies the necessary mathematical conversions and text replacements directly before rendering the story.

## Consequences
This is a simple and effective solution for a binary regional choice, keeping the logic self-contained and easy to understand. However, this approach does not scale well. A more complex application with multiple languages or regions would require a more robust internationalization (i18n) framework with separate resource files for translations and regional formats.