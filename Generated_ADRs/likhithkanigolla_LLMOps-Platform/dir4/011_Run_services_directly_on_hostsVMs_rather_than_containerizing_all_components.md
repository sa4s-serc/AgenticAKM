# ADR-011: Run services directly on hosts/VMs rather than containerizing all components

**Date**: 2025-10-09
**Status**: Proposed

## Context
There are no Dockerfiles or multi-service container manifests, except Kafka’s docker-compose; Vagrant is used for hosts/VMs.

## Decision
Operate most services as native processes on VMs/hosts instead of packaging them into containers.

## Consequences
Pros: simpler runtime model, avoids container overhead, easy for quick scripts. Cons: dependency conflicts, less isolation, harder rollbacks/updates, reduced portability and scalability compared to container orchestrators.