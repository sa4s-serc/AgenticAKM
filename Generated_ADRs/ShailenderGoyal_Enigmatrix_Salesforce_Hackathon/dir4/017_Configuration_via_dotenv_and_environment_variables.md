# ADR-017: Configuration via dotenv and environment variables

**Date**: 2025-10-16
**Status**: Proposed

## Context
Secrets and environment-specific settings must be externalized.

## Decision
Load configuration from .env files using dotenv across server services.

## Consequences
Simplifies local development and deployment; requires secret rotation practices and CI/CD injection; a config schema/validator can prevent runtime misconfigurations.