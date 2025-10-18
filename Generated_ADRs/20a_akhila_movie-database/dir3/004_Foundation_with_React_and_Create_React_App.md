# ADR-004: Foundation with React and Create React App

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project required a modern, industry-standard foundation for building a dynamic Single-Page Application (SPA) while minimizing initial setup and configuration complexity.

## Decision
React was chosen as the core UI library for its component-based model and vast ecosystem. The project was bootstrapped with Create React App (CRA) to provide a pre-configured, opinionated toolchain for development, testing, and building.

## Consequences
This provides a highly productive development experience with features like hot-reloading out of the box. However, it abstracts away the underlying build configuration (Webpack), which can limit advanced customizations without 'ejecting' and taking on the full maintenance burden of the build process.