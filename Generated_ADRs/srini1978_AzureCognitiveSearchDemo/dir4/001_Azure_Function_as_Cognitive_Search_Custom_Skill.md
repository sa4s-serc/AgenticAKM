# ADR-001: Azure Function as Cognitive Search Custom Skill

**Date**: 2025-10-09
**Status**: Proposed

## Context
The repository centers on a .NET Azure Functions project exposing an HTTP endpoint consumed by Azure Cognitive Search skillsets.

## Decision
Implement the enrichment as an Azure Function custom skill rather than as a built-in skill or separate service.

## Consequences
Simplifies integration with Cognitive Search via the native custom skill contract and enables serverless scaling, but introduces Azure Functions operational dependencies (hosting, cold starts, function app configuration) and requires maintaining the function’s API contract across search pipeline changes.