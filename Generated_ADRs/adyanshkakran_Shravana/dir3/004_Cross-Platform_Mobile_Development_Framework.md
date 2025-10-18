# ADR-004: Cross-Platform Mobile Development Framework

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project required a mobile application that could run on both iOS and Android to maximize market reach, while also being mindful of development time and resource constraints.

## Decision
To use React Native with the Expo framework for mobile app development. This choice allows for a single JavaScript/TypeScript codebase to serve both platforms, with UI accelerated by component libraries like Native Base and React Native Paper.

## Consequences
This approach reduces development time and cost by avoiding the need for two separate native codebases. The trade-off is potential performance limitations for highly complex or graphically intensive features compared to pure native development. It also creates a dependency on the React Native and Expo ecosystems for updates and access to native functionalities.