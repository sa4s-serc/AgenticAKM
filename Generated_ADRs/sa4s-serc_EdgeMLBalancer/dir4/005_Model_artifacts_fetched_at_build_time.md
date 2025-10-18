# ADR-005: Model artifacts fetched at build time

**Date**: 2025-10-10
**Status**: Proposed

## Context
A download_models.gradle script indicates models are retrieved during builds rather than stored in VCS.

## Decision
Externalize model binaries and download them during the Gradle build.

## Consequences
Reduces repository size and licensing friction but adds network/build reproducibility dependencies, potential supply-chain risks, and the need to pin and verify model sources and checksums.