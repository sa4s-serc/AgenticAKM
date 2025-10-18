# ADR-008: Repository structure favors side-by-side variants over a single integrated module

**Date**: 2025-10-10
**Status**: Proposed

## Context
There is a "Main code/" Android project, a separate top-level "app/" module, and standalone fragment variants outside a single Gradle module.

## Decision
Organize multiple versions and experiment directories alongside the main project rather than integrating them into a unified multi-module build.

## Consequences
Simplifies ad-hoc experimentation but complicates onboarding, CI configuration, and dependency sharing; requires clear documentation on the canonical build target and how to switch variants.