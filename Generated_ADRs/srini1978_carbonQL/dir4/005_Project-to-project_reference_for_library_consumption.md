# ADR-005: Project-to-project reference for library consumption

**Date**: 2025-10-09
**Status**: Proposed

## Context
The console build output includes carbonQLBackend.dll copied alongside, indicating a direct project reference.

## Decision
Consume the backend via a direct project reference rather than a packaged artifact.

## Consequences
Streamlines local development and synchronized versioning. Reduces friction for internal changes but complicates external distribution and versioned dependency management compared to NuGet packaging.