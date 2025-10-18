# ADR-006: Hybrid File Storage Strategy for User Uploads

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application required a mechanism to handle user-generated image uploads for profiles and communities. The solution needed to be simple for development but also have a path toward a scalable, production-ready implementation.

## Decision
A hybrid approach to file storage was adopted. The system uses local filesystem storage (`/public/images`) via Multer, which is straightforward for a single-server environment. Additionally, the presence of `onedrive.js` indicates a planned or implemented integration with a cloud storage provider.

## Consequences
The local storage solution is simple and works well for development but is not viable for a production environment with multiple server instances or ephemeral containers. The integration with cloud storage is a critical design choice for scalability, persistence, and reliability, as it decouples file assets from the application server's lifecycle. This dual strategy reflects a pragmatic approach, addressing both immediate development needs and future production requirements.