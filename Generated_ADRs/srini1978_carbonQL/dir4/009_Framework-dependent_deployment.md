# ADR-009: Framework-dependent deployment

**Date**: 2025-10-09
**Status**: Proposed

## Context
Console output includes deps.json and runtimeconfig.json; no self-contained publish artifacts are indicated.

## Decision
Distribute framework-dependent binaries rather than self-contained executables.

## Consequences
Smaller artifacts and faster builds but requires target environments to have a compatible .NET runtime installed. Self-contained publication would increase size but improve portability and isolation.