# ADR-014: Broad runtime compatibility across Node versions and platforms

**Date**: 2025-10-10
**Status**: Proposed

## Context
Workshops and contributors use diverse environments that should run the app without friction.

## Decision
Support Node.js engines 18–22 and multiple OS/CPU architectures as declared in package.json and validated in CI.

## Consequences
Benefits: larger contributor base and fewer environment blockers. Drawbacks: expanded test matrix, need for polyfills or conditional code paths, higher risk of subtle environment-specific issues.