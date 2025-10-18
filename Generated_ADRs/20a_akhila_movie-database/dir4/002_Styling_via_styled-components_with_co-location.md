# ADR-002: Styling via styled-components with co-location

**Date**: 2025-10-10
**Status**: Proposed

## Context
Components pair index.js with corresponding *.styles.js files and a GlobalStyle.js sets global CSS.

## Decision
Adopt styled-components for component-scoped styling and colocate style definitions alongside components.

## Consequences
Scoped, themeable styles and reduced classname collisions; runtime CSS-in-JS overhead and potential performance costs; extracting critical CSS or SSR styling would require additional work.