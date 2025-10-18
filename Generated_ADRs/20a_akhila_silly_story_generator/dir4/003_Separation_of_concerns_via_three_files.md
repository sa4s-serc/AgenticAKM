# ADR-003: Separation of concerns via three files

**Date**: 2025-10-10
**Status**: Proposed

## Context
Maintain readability and modularity for a small codebase.

## Decision
Split responsibilities into index.html (markup), style.css (styling), and index.js (behavior).

## Consequences
Clear structure and maintainability, browser caching benefits for CSS/JS; remains simplistic for scaling beyond a small app.