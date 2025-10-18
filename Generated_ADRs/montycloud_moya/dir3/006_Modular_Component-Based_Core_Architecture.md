# ADR-006: Modular, Component-Based Core Architecture

**Date**: 2025-10-11
**Status**: Proposed

## Context
Building a robust framework for complex systems requires a design that is easy to understand, maintain, and extend over time. A monolithic design would quickly become unmanageable.

## Decision
To structure the entire framework around key, decoupled components with clear responsibilities: Agents (actors), Orchestrators (coordinators), Tools (capabilities), and Memory (state). This enforces a strong separation of concerns.

## Consequences
The resulting architecture is highly maintainable and extensible. Each component can be developed, tested, and replaced independently. This modularity makes it easy for developers to understand the system and contribute new functionality, such as a custom orchestrator or a new type of agent.