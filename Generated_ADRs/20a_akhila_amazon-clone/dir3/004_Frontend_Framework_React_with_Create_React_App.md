# ADR-004: Frontend Framework: React with Create React App

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project required a dynamic and interactive user interface to replicate the rich functionality of an e-commerce site like Amazon. A component-based approach was desired for UI reusability and maintainability.

## Decision
React was chosen as the frontend library. The project was bootstrapped using Create React App (CRA) to standardize the development environment and build toolchain.

## Consequences
React's component model promotes a modular and maintainable codebase. The vast ecosystem provides a wide range of libraries for UI, routing, and other needs. Using CRA simplifies the configuration but also abstracts away the underlying build tools (like Webpack), which can limit custom configuration options if needed later.