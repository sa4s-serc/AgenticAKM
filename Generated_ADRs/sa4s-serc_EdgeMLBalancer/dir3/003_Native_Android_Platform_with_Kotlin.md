# ADR-003: Native Android Platform with Kotlin

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application requires tight integration with the Android operating system for core functionalities, including direct camera access, sensor data for health monitoring, and high-performance graphics rendering for the overlay. Maximum performance and responsiveness were critical requirements.

## Decision
The application was built as a native Android app using Kotlin as the primary programming language. This provides direct, high-performance access to the Android SDK, hardware APIs (like CameraX), and platform-specific performance optimization opportunities.

## Consequences
This choice results in a highly performant and responsive application that can fully leverage device hardware. The trade-off is a lack of cross-platform portability; the codebase is specific to Android and cannot be reused for other operating systems like iOS.