---
### ADR-005: Use a Custom Bridge Network with Static IP Addresses

Status: Inferred
Context: docker-compose.yml defines a user-defined network with IPAM and assigns fixed IPv4 addresses to services (172.22.0.2 and 172.22.0.3). This enforces deterministic addressing between services.
Decision: Configure a dedicated Docker bridge network with static IPs for inter-service communication.
Consequences: Predictable service addressing can simplify integration/testing and documentation. However, it increases operational overhead, risks IP conflicts, and bypasses Docker’s built-in service name DNS resolution, reducing flexibility and scalability.