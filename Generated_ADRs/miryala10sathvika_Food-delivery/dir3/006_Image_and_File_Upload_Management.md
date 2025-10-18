# ADR-006: Image and File Upload Management

**Date**: 2025-10-13
**Status**: Proposed

## Context
The system required a mechanism for administrators to upload product images. This functionality needed to be integrated cleanly into the existing Node.js/Express backend.

## Decision
The `multer` middleware for Express.js was implemented to handle `multipart/form-data` requests. This allows the backend to efficiently process file uploads, specifically images for food items, submitted from the admin panel.

## Consequences
Multer provides a straightforward and robust solution for handling file uploads within the Node.js ecosystem. This choice keeps file management logic encapsulated on the server-side and integrates seamlessly with the existing API structure, allowing images to be associated with product data in the database.