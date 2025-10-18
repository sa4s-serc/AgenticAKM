# ADR-004: Node/Express backend using classic Express-generator structure with Jade views

**Date**: 2025-10-14
**Status**: Proposed

## Context
The backend includes app.js, bin/www.js, routes/*, and views/*.jade, indicating server-side templating alongside an API.

## Decision
Use Express as the backend with a mix of JSON API endpoints and server-rendered pages using Jade/Pug templates.

## Consequences
Offers flexibility for rendering certain pages (e.g., error or utility pages) while powering the SPA with APIs; increases cognitive load by mixing rendering modes and requires clear ownership of UI concerns to avoid duplication.