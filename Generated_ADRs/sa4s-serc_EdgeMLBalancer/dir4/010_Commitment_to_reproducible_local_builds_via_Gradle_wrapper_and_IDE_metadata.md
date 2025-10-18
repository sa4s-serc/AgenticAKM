# ADR-010: Commitment to reproducible local builds via Gradle wrapper and IDE metadata

**Date**: 2025-10-10
**Status**: Proposed

## Context
Gradle wrapper, project settings, and Android Studio metadata (.idea/, .gradle/) are present.

## Decision
Check in the Gradle wrapper and development environment metadata to ease setup.

## Consequences
Improves build reproducibility and onboarding at the cost of a larger repository and potential for stale IDE configuration to affect contributors.