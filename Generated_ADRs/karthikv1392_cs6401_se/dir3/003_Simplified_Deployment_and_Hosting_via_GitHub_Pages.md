# ADR-003: Simplified Deployment and Hosting via GitHub Pages

**Date**: 2025-10-08
**Status**: Proposed

## Context
The project required a zero-cost, highly available, and automated hosting and deployment solution that would minimize the operational burden on the course administrators.

## Decision
The system was architected for native integration with GitHub Pages. The inclusion of the `github-pages` gem standardizes the build environment, enabling a fully automated CI/CD pipeline where a `git push` to the main branch triggers a new build and deployment.

## Consequences
This provides a free, reliable, and 'zero-ops' hosting solution with an integrated CI/CD process. The site benefits from GitHub's global CDN for fast content delivery. The primary limitation is the restriction to static site hosting and a dependency on the GitHub platform's specific build environment and supported plugins.