# ADR-003: Hardware Abstraction for Heterogeneous Edge Deployment

**Date**: 2025-10-14
**Status**: Proposed

## Context
Edge devices vary significantly in their computational hardware, including standard CPUs, NVIDIA GPUs, and specialized accelerators like Intel NPUs. To be broadly applicable, the system must perform optimally on diverse hardware.

## Decision
An abstraction layer was implemented in the edge client to support multiple hardware backends. The system can dynamically target CPU, CUDA (for NVIDIA GPUs), or OpenVINO (for Intel NPUs) without changing the core application logic.

## Consequences
This decision grants the system significant flexibility and portability, allowing it to be deployed across a wide range of hardware. The cost is increased complexity in the codebase, requiring maintenance and testing for multiple execution paths and hardware-specific dependency sets.