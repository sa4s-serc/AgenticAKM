# ADR-005: Configuration and Secrets Handling

**Date**: 2025-10-09
**Status**: Proposed

## Context
Indications of hardcoded credentials/config; local.settings.json is present with placeholders.

## Decision
Initial implementation appears to embed Bing configuration in code; recommended to externalize keys and config to function app settings and/or Key Vault.

## Consequences
Hardcoded secrets risk leakage and complicate rotation; externalizing enables secure secret governance, environment-specific configuration, and safer CI/CD, at the cost of added setup (app settings/Key Vault integration).