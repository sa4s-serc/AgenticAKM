# ADR-001: SPA foundation with Create React App

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application is a single-page movie browser mounted via index.js and built with react-scripts.

## Decision
Bootstrap the frontend with Create React App and run as a client-only SPA.

## Consequences
Rapid setup and standardized tooling with HMR and common scripts; limited control over the build pipeline without ejecting; no server-side rendering out of the box, which impacts initial load and SEO.