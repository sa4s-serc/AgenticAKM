# ADR-001: SPA via Create React App on Firebase Hosting

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project is scaffolded with Create React App (react-scripts 4) and includes firebase.json/.firebaserc and a .firebase cache, indicating Firebase Hosting is used.

## Decision
Build a client-rendered single-page application (SPA) with CRA and deploy static assets to Firebase Hosting.

## Consequences
Fast local development and simple deployment; no server-side rendering out of the box, which can impact SEO and time-to-first-byte for initial loads; CRA v4 has slower builds and older tooling compared with newer bundlers (e.g., Vite) or frameworks (e.g., Next.js).