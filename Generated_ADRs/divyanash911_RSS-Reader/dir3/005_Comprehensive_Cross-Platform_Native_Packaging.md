# ADR-005: Comprehensive Cross-Platform Native Packaging

**Date**: 2025-10-13
**Status**: Proposed

## Context
To reach a wider audience and provide a seamless installation experience for end-users on various desktop operating systems, the application needed to be distributed as more than just a runnable JAR or Docker image.

## Decision
Implement a build process using specialized Maven plugins (`jdeb`, `rpm-maven-plugin`, `nsis-maven-plugin`, etc.) to generate native installers for Debian, Red Hat, Windows, and macOS.

## Consequences
This significantly enhances the user experience and accessibility of the application for non-technical users. However, it dramatically increases the complexity and maintenance burden of the build system, as each platform's packaging has its own unique configuration requirements and potential issues.