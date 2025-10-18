# ADR-001: Full-stack monorepo using Angular SPA and Express/TypeScript backend

**Date**: 2025-10-10
**Status**: Proposed

## Context
The app must deliver a modern web UI and an API in a single deployable for training and CTF use while remaining accessible to contributors.

## Decision
Keep frontend under frontend/ built with Angular CLI and a Node.js/TypeScript Express backend (entry points app.ts and server.ts) in the same repo, with integrated build and serve flows.

## Consequences
Benefits: cohesive developer experience, simplified end-to-end changes, consistent TypeScript tooling across stack. Drawbacks: tighter coupling between UI and API, larger install/build times (postinstall FE build), more complex CI caching.