# ADR-011: Web frontend on AngularJS 1.x with jQuery and in-browser Less

**Date**: 2025-10-14
**Status**: Proposed

## Context
Web module assets include AngularJS 1.x, Angular UI Bootstrap 0.12, jQuery 2.1.3, and Less 2.3.1 compiled in the browser.

## Decision
Build a single-page app using AngularJS 1.x and Bootstrap, compiling Less on the client.

## Consequences
Rapid development with established libraries (at the time) but now legacy and EOL; security and maintenance risks; client-side Less compilation adds runtime overhead; migration to a modern framework is advisable.