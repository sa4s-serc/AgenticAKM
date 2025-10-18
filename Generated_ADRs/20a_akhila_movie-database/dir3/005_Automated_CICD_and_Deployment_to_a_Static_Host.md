# ADR-005: Automated CI/CD and Deployment to a Static Host

**Date**: 2025-10-10
**Status**: Proposed

## Context
An automated, reliable, and repeatable process was needed for building, testing, and deploying the application from the source code repository to a live environment.

## Decision
A DevOps pipeline was established using GitLab CI/CD, as defined by the `.gitlab-ci.yml` file. The target deployment platform is Netlify, a hosting service optimized for static assets and SPAs.

## Consequences
This enables a streamlined GitOps workflow where code changes are automatically deployed, increasing development velocity and reducing manual errors. Netlify provides high performance via its global CDN and simplifies the hosting process. The architecture is now coupled to the GitLab and Netlify platforms, which would require effort to migrate from in the future.