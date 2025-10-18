# ADR-003: Custom in-repo Service Registry instead of a standard solution

**Date**: 2025-10-09
**Status**: Proposed

## Context
service-registry/ provides registry.py with bootstrap scripts; no references to Consul, etcd, or Eureka are present.

## Decision
Implement a bespoke service registry to track/resolve service locations rather than adopting a production-grade discovery system.

## Consequences
Pros: minimal dependencies, tailored functionality, quick to stand up. Cons: single point of failure, limited health checking and consistency guarantees, lacks ecosystem features (ACLs, TTL/leases, UI), and increased maintenance burden.