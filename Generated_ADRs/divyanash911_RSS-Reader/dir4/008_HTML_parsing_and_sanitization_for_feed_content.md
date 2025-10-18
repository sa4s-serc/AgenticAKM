# ADR-008: HTML parsing and sanitization for feed content

**Date**: 2025-10-13
**Status**: Proposed

## Context
Dependencies include TagSoup and OWASP HTML Sanitizer, common for cleaning and normalizing HTML.

## Decision
Normalize and sanitize feed content using TagSoup and OWASP HTML Sanitizer prior to storage/rendering.

## Consequences
Mitigates XSS and malformed HTML risks; improves display consistency; may strip or alter some formatting; adds CPU overhead during ingestion.