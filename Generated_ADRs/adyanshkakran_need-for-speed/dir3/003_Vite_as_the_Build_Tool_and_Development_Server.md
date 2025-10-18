# ADR-003: Vite as the Build Tool and Development Server

**Date**: 2025-10-14
**Status**: Proposed

## Context
A modern web application with a modular JavaScript codebase requires an efficient build system and a productive development environment. Key needs included fast startup, hot module replacement (HMR), and optimized production builds.

## Decision
Vite was selected as the sole development dependency for the build process and local development server. It is configured to handle module resolution, asset bundling, and provide a fast feedback loop with HMR.

## Consequences
The development workflow is significantly accelerated due to Vite's native ES module-based server and rapid HMR. It simplifies configuration compared to older bundlers. The project is now dependent on the Vite ecosystem and its specific build pipeline for creating production-ready assets.