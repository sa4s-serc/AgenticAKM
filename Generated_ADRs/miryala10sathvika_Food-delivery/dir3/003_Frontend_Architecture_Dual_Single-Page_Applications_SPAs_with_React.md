# ADR-003: Frontend Architecture: Dual Single-Page Applications (SPAs) with React

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application required a modern, dynamic, and responsive user experience for both customers and administrators, without the need for full page reloads on every interaction. A fast development workflow was also a key requirement.

## Decision
Two separate Single-Page Applications (SPAs) were created using React: one for the customer-facing site and another for the admin panel. Vite was chosen as the build tool for its fast development server and optimized builds. `react-router-dom` handles client-side navigation.

## Consequences
This approach delivers a fluid, app-like user experience. The component-based nature of React promotes code reusability and maintainability. Separating the admin and customer frontends creates a strong security and functional boundary. Vite significantly improves the developer experience with near-instantaneous hot module replacement.