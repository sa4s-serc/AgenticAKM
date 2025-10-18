# ADR-008: Control plane (controller/deployer) separated from agent execution

**Date**: 2025-10-09
**Status**: Proposed

## Context
controller-Service/controller.py, deployer-service/server.py, agent-Service/agent.py, and vm-service/agent.py indicate distinct control components and host/VM agents.

## Decision
Split orchestration responsibilities (controller and deployer) from execution responsibilities (agents on hosts/VMs).

## Consequences
Pros: clear separation of concerns, easier horizontal scaling of execution nodes, supports heterogeneous runtimes. Cons: requires secure and reliable control-to-agent communication, complex failure handling/rollback, and agent lifecycle management.