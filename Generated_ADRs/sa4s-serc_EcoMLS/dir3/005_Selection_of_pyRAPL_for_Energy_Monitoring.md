# ADR-005: Selection of `pyRAPL` for Energy Monitoring

**Date**: 2025-10-10
**Status**: Proposed

## Context
To implement the 'Monitor' component of the MAPEK-K loop, a concrete technology was needed to measure the primary optimization metric: energy consumption. The measurement needed to be accessible programmatically from Python.

## Decision
The `pyRAPL` library was chosen to monitor energy consumption. This tool interfaces directly with Intel's Running Average Power Limit (RAPL) hardware counters on the CPU to provide power and energy readings.

## Consequences
This provides access to relatively accurate, hardware-level energy data for the CPU and DRAM, which is more reliable than purely model-based estimates. However, this decision creates a hardware dependency; the system's energy monitoring will only function on Intel CPUs that support RAPL. Furthermore, it may not capture the energy consumption of other critical components in an ML system, most notably a dedicated GPU.