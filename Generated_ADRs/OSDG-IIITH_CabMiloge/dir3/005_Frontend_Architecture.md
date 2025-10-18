# ADR-005: Frontend Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application needed a functional and responsive user interface for users to manage their profiles and trips. The complexity of the UI did not warrant a heavy client-side framework.

## Decision
A traditional server-side rendering (SSR) approach was adopted using the Jinja2 templating engine integrated with Flask. Vanilla JavaScript is used for minimal client-side dynamic interactions, and modern CSS3 (Flexbox) is used for styling.

## Consequences
This results in a lightweight, fast-loading frontend that is tightly coupled with the backend, simplifying development. It avoids the complex build toolchains associated with modern Single-Page Applications (SPAs). However, for highly interactive or complex future features, managing UI state with vanilla JavaScript could become difficult, and the user experience might feel less fluid than that of an SPA.