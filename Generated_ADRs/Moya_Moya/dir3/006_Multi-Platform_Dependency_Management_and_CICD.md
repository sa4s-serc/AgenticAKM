# ADR-006: Multi-Platform Dependency Management and CI/CD

**Date**: 2025-10-14
**Status**: Proposed

## Context
For an open-source library to achieve widespread adoption and be considered enterprise-grade, it must be easy to integrate into various project setups and maintain a high standard of code quality and stability.

## Decision
To officially support all major Swift dependency managers (CocoaPods, Carthage, Swift Package Manager) and to implement a robust CI/CD pipeline using tools like CircleCI, SwiftLint for code quality, and Danger for automated PR checks.

## Consequences
This broad support lowers the barrier to adoption for developers. The professional-grade tooling and CI/CD process ensure high code quality, project stability, and maintainability, establishing trust and making Moya a reliable choice for projects of any size.