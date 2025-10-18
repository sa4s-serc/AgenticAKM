# ADR-002: Architectural Pattern: Separation of Concerns (SoC)

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application's codebase needed to be structured in a clear and maintainable way. The primary aspects of the application are its structure, visual presentation, and interactive behavior.

## Decision
To adopt the classic web architecture of separating concerns into distinct files: `index.html` for structure, `style.css` for presentation, and `index.js` for all application logic and behavior.

## Consequences
This decision promotes a clean, organized, and easily maintainable codebase. It allows developers and designers to work on different aspects of the application independently. For a project of this small scale, this approach is highly effective and easy to reason about.