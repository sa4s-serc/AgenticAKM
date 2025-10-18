# ADR-012: Environment-driven configuration for LLMs and external services

**Date**: 2025-10-14
**Status**: Proposed

## Context
LLM provider details and external service configurations are not embedded; settings are implied via environment and config files.

## Decision
Avoid hardcoding providers/keys; rely on environment variables and config for runtime binding.

## Consequences
Pros: safer secret handling, easier environment parity and provider switching. Cons: increases setup complexity; misconfiguration is a common source of runtime errors.