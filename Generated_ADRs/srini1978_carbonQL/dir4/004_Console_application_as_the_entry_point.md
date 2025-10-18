# ADR-004: Console application as the entry point

**Date**: 2025-10-09
**Status**: Proposed

## Context
carbonQLConsole contains Program.cs and runs the backend logic.

## Decision
Use a console app as the primary interaction surface.

## Consequences
Simplifies execution and local development; suitable for batch/CLI scenarios. Limits discoverability and integration compared to a web API or GUI and may require rework if a service-based interface is needed.