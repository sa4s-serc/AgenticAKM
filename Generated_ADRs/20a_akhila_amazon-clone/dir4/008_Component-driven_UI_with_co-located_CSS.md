# ADR-008: Component-driven UI with co-located CSS

**Date**: 2025-10-10
**Status**: Proposed

## Context
Components (Header, Home, Product, Checkout, etc.) have adjacent CSS files; multiple UI libraries are declared.

## Decision
Build feature-focused React components with per-component CSS, while allowing usage of third-party UI kits where helpful.

## Consequences
Clear separation and maintainability at small/medium scale; risk of style leakage and specificity issues; mixing libraries (MUI, Bootstrap, emotion) can increase bundle size, duplicate design primitives, and introduce theming inconsistencies.