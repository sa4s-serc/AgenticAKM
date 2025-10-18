# ADR-004: Component-Based UI via a Templating System

**Date**: 2025-10-08
**Status**: Proposed

## Context
The website needed to maintain a consistent visual identity and structure across all pages. A mechanism was required to manage common UI elements (headers, footers, navigation) centrally to simplify maintenance and future design changes.

## Decision
A modular templating architecture was adopted using Jekyll's `_layouts` and `_includes` directories. Reusable UI components are defined as partials in `_includes`, and overall page structures are defined in `_layouts`, ensuring a consistent and maintainable presentation layer.

## Consequences
This approach enforces design consistency, promotes code reuse (DRY principle), and makes site-wide visual updates highly efficient. Any changes to the header or navigation, for example, only need to be made in one place. The main dependency is on the Liquid templating language, which developers must learn to modify the site's structure.