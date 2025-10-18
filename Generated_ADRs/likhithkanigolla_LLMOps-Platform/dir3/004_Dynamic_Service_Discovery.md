# ADR-004: Dynamic Service Discovery

**Date**: 2025-10-09
**Status**: Proposed

## Context
In a distributed microservices environment, services are ephemeral and their network locations (IP, port) are not fixed. A mechanism was needed for services to find and communicate with each other dynamically.

## Decision
A dedicated Service Registry was implemented. Every service registers its location upon startup, and other services query the registry to discover the current address of any service they need to communicate with.

## Consequences
This enables loose coupling and location transparency, eliminating the need for hardcoded network locations and simplifying configuration. The Service Registry itself becomes a critical system component; if it fails, inter-service communication breaks down, making its high availability essential.