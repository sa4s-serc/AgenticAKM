# ADR-001: Multi-Module Maven Architecture

**Date**: 2025-10-13
**Status**: Proposed

## Context
The project required a clear separation of concerns to manage complexity, facilitate parallel development, and ensure maintainability as a non-trivial web application. Different logical components like core business logic, web-specific code, and packaging needed to be isolated.

## Decision
The project was structured as a multi-module Maven project, with distinct modules for `reader-core`, `reader-web-common`, and `reader-web`. Build profiles were used to further separate application logic from platform-specific packaging concerns.

## Consequences
This enforces a clean architecture, making the codebase easier to navigate and understand. It allows for independent builds and testing of components, but also introduces a higher level of build configuration complexity that must be managed, especially regarding inter-module dependencies.