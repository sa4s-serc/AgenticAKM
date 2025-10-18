# ADR-010: Process orchestration via Python scripts and filesystem

**Date**: 2025-10-10
**Status**: Proposed

## Context
Experiments must coordinate input handling, archiving, and run control without introducing a message bus or task queue.

## Decision
Use a Python coordinator (Node.py) and utility scripts for starting/stopping processes and managing files, rather than distributed services or queues.

## Consequences
Minimizes dependencies and complexity; adequate for single-host prototypes; limits fault tolerance, observability, and scalability; brittle under failures and hard to distribute across nodes.