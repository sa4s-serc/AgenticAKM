# ADR-001: Adoption of a Static Site Generator (Jekyll)

**Date**: 2025-10-08
**Status**: Proposed

## Context
The project required a robust, secure, and low-maintenance platform to deliver university course materials. Key requirements included high performance, low operational overhead, and ease of content updates by technically proficient staff.

## Decision
The architecture is centered on Jekyll, a static site generator. All content is pre-compiled into a complete website of static HTML, CSS, and asset files during a build step, eliminating the need for a server-side runtime or database.

## Consequences
This results in a highly performant and secure website with minimal hosting requirements, as serving static files is trivial. It simplifies the deployment pipeline and reduces operational costs. However, it precludes dynamic server-side functionality, requiring third-party services for features like forms or real-time updates.