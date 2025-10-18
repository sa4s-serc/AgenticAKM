# ADR-007: Prebuilt debug APK checked into the repository

**Date**: 2025-10-10
**Status**: Proposed

## Context
app-debug.apk is shipped at the repository root for quick sideloading.

## Decision
Distribute a prebuilt debug artifact to streamline evaluation without building from source.

## Consequences
Accelerates trials and demos but may drift from source, uses a debug keystore, increases repo size, and creates ambiguity about the canonical build output.