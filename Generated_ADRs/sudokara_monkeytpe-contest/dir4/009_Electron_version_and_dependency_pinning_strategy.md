# ADR-009: Electron version and dependency pinning strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
package.json specifies electron as a devDependency with a caret range (^37.4.0) and includes a package‑lock.json.

## Decision
Target a modern Electron major version with semver‑compatible auto‑updates within the range and rely on lockfile for reproducible installs.

## Consequences
Access to up‑to‑date Chromium/Node features and security fixes, but caret updates can introduce behavior changes; OS/runtime requirements increase, and ongoing maintenance is needed to track Electron releases.