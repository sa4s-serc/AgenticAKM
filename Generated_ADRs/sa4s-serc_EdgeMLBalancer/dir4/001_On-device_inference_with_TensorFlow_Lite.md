# ADR-001: On-device inference with TensorFlow Lite

**Date**: 2025-10-10
**Status**: Proposed

## Context
The app performs object detection directly on Android devices and surfaces inference metrics in the UI.

## Decision
Use TensorFlow Lite for fully on-device inference instead of server-side processing.

## Consequences
Eliminates network latency and preserves privacy/offline use, but shifts performance, thermal, and power costs to the device and requires careful optimization and device-compatibility testing.