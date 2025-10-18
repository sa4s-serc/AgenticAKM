# ADR-004: 12-factor configuration via environment files

**Date**: 2025-10-14
**Status**: Proposed

## Context
.env.template is included and Docker/Compose typically inject env vars.

## Decision
Externalize configuration to environment variables, templated via .env files.

## Consequences
- Clean separation of config from code; easy per-environment overrides
- Lower risk of committing secrets if .env is excluded correctly
- Requires disciplined secret management (vaults/CI masking) for production
- Simplifies container portability and CI/CD parameterization