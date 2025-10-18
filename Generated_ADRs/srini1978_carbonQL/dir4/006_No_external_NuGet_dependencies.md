# ADR-006: No external NuGet dependencies

**Date**: 2025-10-09
**Status**: Proposed

## Context
Only Microsoft.NETCore.App framework is referenced; no third-party packages are noted.

## Decision
Rely solely on the base .NET runtime libraries.

## Consequences
Minimizes attack surface, licensing concerns, and supply-chain risk. May require custom implementations for concerns like DI, logging, configuration, or serialization, potentially increasing maintenance burden.