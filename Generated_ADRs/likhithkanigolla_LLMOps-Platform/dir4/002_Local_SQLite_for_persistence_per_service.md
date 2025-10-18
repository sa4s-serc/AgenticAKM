# ADR-002: Local SQLite for persistence per service

**Date**: 2025-10-09
**Status**: Proposed

## Context
frontend/users.db and model-registry/model_registry.db are checked into service directories; no external DB configuration is present.

## Decision
Use SQLite files for local persistence of user accounts (frontend) and model metadata (model registry).

## Consequences
Pros: zero-configuration, easy local development, minimal ops burden. Cons: limited concurrency and locking, poor horizontal scalability, challenging backup/HA, and risk of data divergence across nodes or environments.