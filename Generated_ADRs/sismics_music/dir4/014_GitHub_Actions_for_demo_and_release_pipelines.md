# ADR-014: GitHub Actions for demo and release pipelines

**Date**: 2025-10-14
**Status**: Proposed

## Context
CI workflows build-demo.yml and build-release.yml exist in .github/workflows.

## Decision
Automate builds and releases via GitHub Actions with separate demo and release workflows.

## Consequences
Improves reliability and repeatability of builds; must orchestrate both Maven and Gradle, plus multi-OS packaging; caching and matrix strategies are needed to keep pipelines performant.