# ADR-006: File system storage for images on the backend

**Date**: 2025-10-13
**Status**: Proposed

## Context
An images/ directory exists under code/backend.

## Decision
Persist image assets on the server’s local file system instead of an external object storage service.

## Consequences
Simplifies implementation and local development, but complicates horizontal scaling, backup/restore, and CDN delivery; file path security and permissions must be managed.