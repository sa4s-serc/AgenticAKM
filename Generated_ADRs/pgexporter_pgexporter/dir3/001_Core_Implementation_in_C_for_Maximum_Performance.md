# ADR-001: Core Implementation in C for Maximum Performance

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project's goal is to monitor production PostgreSQL databases, including heavily-loaded systems. This requires an exporter with minimal resource consumption (CPU, memory) and low latency to avoid impacting the performance of the database it is monitoring.

## Decision
The exporter was implemented entirely in C, a systems-level programming language known for its performance and fine-grained control over system resources. This is coupled with high-performance libraries like `libev` for event-driven I/O.

## Consequences
This results in a highly efficient, high-throughput binary with a very small footprint, making it suitable for demanding environments. The tradeoff is a higher development complexity and a steeper learning curve for new contributors compared to higher-level languages like Go or Python.