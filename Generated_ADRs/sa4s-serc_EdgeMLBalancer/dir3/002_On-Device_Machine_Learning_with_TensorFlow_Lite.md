# ADR-002: On-Device Machine Learning with TensorFlow Lite

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application's primary function is real-time object detection from a live camera feed. Cloud-based inference would introduce unacceptable latency, incur data costs, and raise privacy concerns. The ML processing had to be performed locally on the device.

## Decision
TensorFlow Lite (TFLite) was chosen as the framework for on-device inference. This allows the application to bundle multiple ML models directly within its assets and execute them on the device's CPU or specialized hardware accelerators without needing a network connection.

## Consequences
This enables a low-latency, real-time user experience and preserves user privacy. However, it makes the application's performance directly dependent on the end-user's device capabilities and increases the application's overall binary size due to the included TFLite runtime and model files.