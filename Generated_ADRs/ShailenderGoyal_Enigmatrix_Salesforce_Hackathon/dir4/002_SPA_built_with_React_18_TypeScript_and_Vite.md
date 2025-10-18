# ADR-002: SPA built with React 18, TypeScript, and Vite

**Date**: 2025-10-16
**Status**: Proposed

## Context
The frontend is implemented as a client-rendered single-page application.

## Decision
Use React 18 with TypeScript and Vite for a modern, fast-build SPA without SSR/Next.js.

## Consequences
Great developer experience, fast HMR, and simple static hosting; weaker SEO and slower first paint than SSR; more client-side responsibility for routing and data fetching.