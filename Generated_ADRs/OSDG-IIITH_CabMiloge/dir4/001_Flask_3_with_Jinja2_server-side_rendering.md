# ADR-001: Flask 3 with Jinja2 server-side rendering

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application is centered on app.py using Flask with multiple Jinja2 HTML templates and static assets.

## Decision
Build a server-rendered web app using Flask 3 and Jinja2 templates rather than a client-side SPA.

## Consequences
- Simple request/response model and SEO-friendly pages
- Tight coupling of Python routes and views; fast iteration for CRUD-style pages
- Limited native support for realtime features (websockets) and long-lived async I/O
- Horizontal scaling is process-based behind a WSGI server