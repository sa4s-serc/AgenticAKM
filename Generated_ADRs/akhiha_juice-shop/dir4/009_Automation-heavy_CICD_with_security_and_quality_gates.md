# ADR-009: Automation-heavy CI/CD with security and quality gates

**Date**: 2025-10-10
**Status**: Proposed

## Context
Open-source project with frequent contributions needs consistent quality, supply-chain oversight, and release automation despite intentional vulns.

## Decision
Use GitHub Actions for CI, CodeQL analysis, Dependabot updates, ZAP scanning, and automated content updates; provide GitLab CI config for portability.

## Consequences
Benefits: early detection of regressions, supply-chain hygiene, predictable releases. Drawbacks: longer CI times and maintenance overhead for multiple workflows/providers; careful tuning needed to separate intended from unintended vulnerabilities.