# ADR-010: No explicit configuration management

**Date**: 2025-10-09
**Status**: Proposed

## Context
No appsettings or configuration files are noted; only standard runtimeconfig.json is present.

## Decision
Operate without externalized application configuration.

## Consequences
Simplifies initial code but risks hard-coded values and environment inflexibility. Introducing environment-specific settings later will require a configuration strategy and potential refactoring.