# ADR-015: SCM linkage to upstream source repository

**Date**: 2025-10-13
**Status**: Proposed

## Context
The parent POM SCM metadata points to https://github.com/sismics/reader, while this snapshot contains no module sources.

## Decision
Keep build and dependency governance in the parent POM while sourcing module code from the upstream repository.

## Consequences
Centralizes version control and build metadata; simplifies project-wide dependency upgrades; necessitates fetching the upstream modules to build; this snapshot alone cannot produce binaries.