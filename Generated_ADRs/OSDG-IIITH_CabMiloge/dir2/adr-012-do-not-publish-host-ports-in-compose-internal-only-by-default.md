---
### ADR-012: Do Not Publish Host Ports in Compose (Internal-Only by Default)

Status: Inferred
Context: docker-compose.yml does not include ports: mappings for either service, and both are placed on a user-defined bridge network.
Decision: Keep services internal to the Docker network by default, without exposing host ports.
Consequences: Improves isolation and reduces accidental exposure. Access from the host requires using container IPs, docker exec/port-forwarding, or adding explicit port mappings/proxying. Mac/Windows workflows may be less straightforward due to differences in Docker networking.