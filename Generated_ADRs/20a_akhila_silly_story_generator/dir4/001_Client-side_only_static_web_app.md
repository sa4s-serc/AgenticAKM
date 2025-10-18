# ADR-001: Client-side only static web app

**Date**: 2025-10-10
**Status**: Proposed

## Context
A simple story generator intended to run entirely in the browser.

## Decision
Deliver the application as static HTML, CSS, and JavaScript with no server or backend APIs.

## Consequences
Offline-capable and zero deployment complexity, easy static hosting, minimal security surface; no persistence, server-side processing, or advanced features like authentication.