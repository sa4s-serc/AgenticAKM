# ADR-003: SPA frontend built with Vite, React, and TypeScript

**Date**: 2025-10-14
**Status**: Proposed

## Context
The frontend uses Vite + React + TypeScript with route-level views and Tailwind CSS configuration; a public/_redirects file is included.

## Decision
Implement the UI as a client-side routed SPA using Vite for fast dev/build, React for components, TypeScript for typing, and Tailwind for utility-first styling.

## Consequences
Delivers fast developer iteration and type safety, and supports static hosting behind Nginx; requires server-side history-fallback configuration, may impact SEO without SSR/Prerendering, and depends on well-defined APIs to minimize client-perceived latency.