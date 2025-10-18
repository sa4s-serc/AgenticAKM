# ADR-013: Front-end asset minification in the build

**Date**: 2025-10-13
**Status**: Proposed

## Context
The parent POM configures plugins for asset minification as part of the web module build.

## Decision
Minify and bundle web assets during the build process.

## Consequences
Improves runtime performance and bandwidth usage; complicates debugging unless source maps are managed; adds potential build fragility when minifiers encounter edge-case inputs.