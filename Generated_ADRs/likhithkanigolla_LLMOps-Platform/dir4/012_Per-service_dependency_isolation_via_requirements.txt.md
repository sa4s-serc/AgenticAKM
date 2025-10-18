# ADR-012: Per-service dependency isolation via requirements.txt

**Date**: 2025-10-09
**Status**: Proposed

## Context
requirements.txt files exist in multiple service directories (frontend, controller-Service, model-registry, agent-Service, deployer-service, etc.).

## Decision
Manage Python dependencies per service using service-local requirements files rather than a monorepo-wide environment.

## Consequences
Pros: clear dependency boundaries, avoids cross-service coupling, simpler upgrades per service. Cons: potential duplication of packages, lack of lockfiles/pinning consistency across services, and increased effort to keep versions aligned for shared libraries.