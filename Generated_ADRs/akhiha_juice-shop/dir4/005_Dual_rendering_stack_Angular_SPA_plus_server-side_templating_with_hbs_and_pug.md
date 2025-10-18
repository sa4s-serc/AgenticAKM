# ADR-005: Dual rendering stack: Angular SPA plus server-side templating with hbs and pug

**Date**: 2025-10-10
**Status**: Proposed

## Context
Training goals require demonstrating both modern SPA issues and classic server-side template vulnerabilities.

## Decision
Retain Angular for the main UI and support server-rendered views with hbs and pug within the Node server.

## Consequences
Benefits: broader vulnerability surface (e.g., XSS, SSTI), flexibility for demo pages and legacy patterns. Drawbacks: larger dependency and attack surface, increased maintenance burden, potential for templating drift with the SPA.