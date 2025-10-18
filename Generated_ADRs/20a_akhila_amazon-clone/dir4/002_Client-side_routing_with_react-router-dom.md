# ADR-002: Client-side routing with react-router-dom

**Date**: 2025-10-10
**Status**: Proposed

## Context
react-router-dom is declared and App.js is present, implying route-based navigation for views like Home, Checkout, Payment, and Orders.

## Decision
Use client-side routing to manage storefront flows within the SPA.

## Consequences
Smooth in-app navigation without full page reloads; requires Firebase Hosting rewrites to serve index.html for deep links; limited SEO compared to SSR; must implement guarded routes for authenticated areas (e.g., Orders, Payment).