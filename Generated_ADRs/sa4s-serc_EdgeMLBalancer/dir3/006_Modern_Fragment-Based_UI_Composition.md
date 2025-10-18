# ADR-006: Modern Fragment-Based UI Composition

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application's user interface needed to be modular to handle distinct states and screens, such as requesting permissions, showing the live camera view, and displaying a detailed performance dashboard (bottom sheet).

## Decision
A modern, single-activity, multi-fragment architecture was adopted. The UI is composed of discrete `Fragment` components (`PermissionsFragment`, `CameraFragment`, `HomeFragment`) that manage their own UI and logic, aligning with Google's recommended best practices for Android development.

## Consequences
This results in a scalable and maintainable UI layer. It simplifies navigation and state management, as each fragment is a self-contained unit of functionality. This is a standard, robust pattern in the Android ecosystem, making the code easier to understand for new developers.