# ADR-001: Adoption of the MAPEK-K Control Loop Architecture

**Date**: 2025-10-10
**Status**: Proposed

## Context
The system required a structured, formal approach to enable self-adaptation at runtime. The goal was to continuously observe the ML application's performance and dynamically adjust its behavior to meet energy and accuracy targets.

## Decision
The architecture was explicitly designed around the MAPEK-K (Monitor-Analyze-Plan-Execute over a Knowledge Base) pattern. Each phase of the control loop is implemented as a distinct component: Monitor.py, Analyzer.py, Planner.py, Execute.py, with a Knowledge Base in a CSV file.

## Consequences
This results in a highly modular and extensible system. The clear separation of concerns makes it easy to understand and maintain. Crucially, it allows for different decision-making strategies (the 'Planner' component) to be swapped out, which is essential for the project's core goal of comparing the advanced EcoMLS strategy against naive baselines. The trade-off is a slight increase in complexity compared to a monolithic design.