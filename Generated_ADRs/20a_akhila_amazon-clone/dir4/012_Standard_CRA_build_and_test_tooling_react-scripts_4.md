# ADR-012: Standard CRA build and test tooling (react-scripts 4)

**Date**: 2025-10-10
**Status**: Proposed

## Context
Scripts are the standard CRA start/build/test/eject with React 17.

## Decision
Use CRA’s default Webpack/Babel configuration without ejecting.

## Consequences
Low maintenance and conventional setup; limited customization without eject or CRACO; older React/tooling versions compared to current best practices (e.g., React 18 concurrent features, faster dev servers); potential performance gaps on large bundles.