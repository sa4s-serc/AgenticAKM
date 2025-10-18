# ADR-007: AzureWebJobsStorage Dependency for Function Host

**Date**: 2025-10-09
**Status**: Proposed

## Context
host.json and local.settings.json indicate standard Azure Functions setup requiring a storage account.

## Decision
Rely on AzureWebJobsStorage for host state/logs even for HTTP triggers.

## Consequences
Adds an operational prerequisite for both local and cloud environments; misconfiguration will prevent the function from starting, and storage availability becomes part of the service reliability envelope.