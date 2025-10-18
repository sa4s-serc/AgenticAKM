# ADR-009: Environment-driven configuration with example.env

**Date**: 2025-10-14
**Status**: Proposed

## Context
The bot requires Meta and OpenAI credentials and runtime settings that vary by environment.

## Decision
Use environment variables (documented in whatsapp-bot/example.env) for all secrets and configuration.

## Consequences
Aligns with 12-factor practices and simplifies secret management; misconfigured environments cause hard-to-debug runtime failures, and local development may require tooling like dotenv or process managers.