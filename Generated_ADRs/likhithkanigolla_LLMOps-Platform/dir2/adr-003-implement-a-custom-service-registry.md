---
### ADR-003: Implement a custom Service Registry

Status: Inferred
Context: A dedicated service-registry/registry.py service and bootstrap scripts exist instead of integrating with established registries (e.g., Consul, etcd, Eureka).
Decision: Build and operate a custom Service Registry service for service discovery and metadata.
Consequences:
- Positive: Tailored functionality and simpler domain-specific behavior; minimal external dependencies.
- Negative: Reinvents proven functionality; requires building health checks, fault-tolerance, and consistency mechanisms that existing products provide.