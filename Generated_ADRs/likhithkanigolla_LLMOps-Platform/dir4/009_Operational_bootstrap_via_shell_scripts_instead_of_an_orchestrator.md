# ADR-009: Operational bootstrap via shell scripts instead of an orchestrator

**Date**: 2025-10-09
**Status**: Proposed

## Context
Multiple bootstrap-*.sh and start.sh scripts exist across services; aside from Kafka docker-compose, there is no Kubernetes or full-service Docker Compose.

## Decision
Rely on shell scripts for environment setup, service bootstrap, and infrastructure tasks instead of standardized orchestration platforms.

## Consequences
Pros: low barrier to entry, fast local bring-up, fewer external dependencies. Cons: environment drift, limited health checks/restarts, manual scaling/rollouts, fragile idempotency, and harder reproducibility across teams and CI/CD.