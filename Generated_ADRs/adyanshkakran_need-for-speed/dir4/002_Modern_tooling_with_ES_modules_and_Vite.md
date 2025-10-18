# ADR-002: Modern tooling with ES modules and Vite

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project targets modern browsers and needs fast local development and bundling.

## Decision
Use ES modules (type: module) and Vite for dev/build/preview.

## Consequences
Gains fast HMR, tree‑shaking, and simple static asset handling; requires modern JS runtime; simplifies deployment but excludes legacy browsers without transpilation.