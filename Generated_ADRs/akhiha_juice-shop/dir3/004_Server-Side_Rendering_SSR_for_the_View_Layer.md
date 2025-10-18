# ADR-004: Server-Side Rendering (SSR) for the View Layer

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application's educational goal is to demonstrate a wide range of web vulnerabilities, many of which are classic and best illustrated in a traditional server-client model. A complex Single-Page Application (SPA) architecture would add unnecessary complexity and be less representative of many systems where these vulnerabilities are found.

## Decision
The view layer is implemented using server-side templating engines (Handlebars and Pug). HTML is generated on the server and sent directly to the client's browser.

## Consequences
This choice simplifies the overall architecture by avoiding a separate frontend framework and build process. It creates an ideal environment for teaching common server-side vulnerabilities like XSS and CSRF. The trade-off is a less fluid user experience with full-page reloads compared to an SPA, which is an acceptable compromise for an educational platform.