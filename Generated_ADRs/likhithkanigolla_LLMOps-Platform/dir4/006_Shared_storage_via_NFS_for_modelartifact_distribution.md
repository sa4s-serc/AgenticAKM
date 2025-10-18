# ADR-006: Shared storage via NFS for model/artifact distribution

**Date**: 2025-10-09
**Status**: Proposed

## Context
bootstrap-service includes boot_nfs_server.sh and boot_nfs_client.sh, indicating reliance on NFS mounts.

## Decision
Use NFS to provide shared POSIX storage across VMs/services for models and artifacts.

## Consequences
Pros: simple, widely supported, minimal application changes. Cons: performance bottlenecks at scale, single point of failure, nuanced permission/security management, and limited multi-tenant isolation.