# ADR-007: Adoption of pyRAPL for Energy Monitoring

**Date**: 2025-10-09
**Status**: Proposed

## Context
To treat energy as a first-class metric, the framework required a programmatic and low-overhead method to measure the power consumption of the ML inference process at runtime.

## Decision
The `pyRAPL` Python library was integrated into the 'Monitor' component. This library provides an interface to Intel's Running Average Power Limit (RAPL) feature, allowing for direct measurement of CPU and DRAM energy usage from within the code.

## Consequences
This enables direct, software-level energy measurement without external hardware, making it possible to log energy consumption as a key performance indicator. The major consequence is a hardware and platform dependency; it primarily works on specific Intel CPUs and may not function correctly in all virtualized or containerized environments. It also typically fails to capture GPU energy usage, a significant limitation for deep learning workloads.