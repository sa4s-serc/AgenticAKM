# ADR-003: Profile-driven module composition and release targeting

**Date**: 2025-10-14
**Status**: Proposed

## Context
Modules like music-core, music-web*, and distribution bundles are wired via the parent POM, with a “prod” profile adding agent and distribution modules.

## Decision
Use Maven profiles to switch between baseline builds and production packaging, enabling targeted inclusion of components.

## Consequences
Speeds up development builds and allows environment-specific outputs; introduces conditional complexity in CI, risk of missing modules in certain builds, and demands clear documentation of profile usage.