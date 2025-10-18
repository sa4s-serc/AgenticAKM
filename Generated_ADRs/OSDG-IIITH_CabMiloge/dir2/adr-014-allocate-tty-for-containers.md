---
### ADR-014: Allocate TTY for Containers

Status: Inferred
Context: docker-compose.yml sets tty: true for both services.
Decision: Allocate a TTY for containers to facilitate interactive debugging and tooling.
Consequences: Makes interactive sessions and certain tooling easier. In production, TTY allocation is generally unnecessary and can affect how logs are handled; should be reviewed for non-development deployments.