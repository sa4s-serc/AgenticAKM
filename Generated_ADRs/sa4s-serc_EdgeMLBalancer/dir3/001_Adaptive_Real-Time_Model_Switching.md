# ADR-001: Adaptive Real-Time Model Switching

**Date**: 2025-10-10
**Status**: Proposed

## Context
Mobile devices have heterogeneous hardware and operate under strict resource constraints (battery, thermal limits). Running a single, high-performance ML model continuously can lead to poor user experience due to battery drain and thermal throttling. The application needed a way to balance inference quality with device health.

## Decision
An adaptive performance management system was architected to dynamically switch between multiple, pre-packaged TensorFlow Lite models (e.g., `EfficientDet-lite0`, `EfficientDet-lite1`) at runtime. The selection is driven by real-time monitoring of device metrics like CPU usage, power consumption, and battery level.

## Consequences
This core decision creates an intelligent, resource-aware system that optimizes the trade-off between performance and efficiency. It enhances robustness across a wide range of devices but introduces significant complexity in managing the state, monitoring device health, and implementing the decision-making (scheduling) logic. The overhead of model loading/unloading must be carefully managed to avoid performance stutters.