# ADR-001: Platform choice: .NET 7 (STS) for all projects

**Date**: 2025-10-09
**Status**: Proposed

## Context
Both carbonQLBackend and carbonQLConsole target net7.0 per the project outputs and structure.

## Decision
Standardize on .NET 7 for the solution.

## Consequences
Leverages modern runtime features and performance, but .NET 7 has short-term support, requiring an upgrade path (e.g., to .NET 8 LTS) to avoid security and support gaps. Consumers must have a compatible .NET 7+ runtime.