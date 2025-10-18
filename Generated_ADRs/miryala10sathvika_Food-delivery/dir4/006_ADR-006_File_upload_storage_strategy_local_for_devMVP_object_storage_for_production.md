# ADR-006: ADR-006: File upload storage strategy (local for dev/MVP, object storage for production)

**Date**: 2025-10-13
**Status**: Proposed

## Context
Uploaded images are present under backend/uploads, indicating local filesystem persistence. This directory is currently tracked in git.

## Decision
Use local filesystem storage at backend/uploads for development and MVP. For production, adopt object storage (e.g., S3) fronted by a CDN. Implement a storage abstraction (e.g., services/storage) with pluggable backends selected by env (STORAGE_BACKEND=local|s3), ensuring consistent URL generation. Reference ADR-011 for VCS policy governing uploads and history cleanup.

## Consequences
- Development remains simple with minimal dependencies.
- Production gains scalability and durability via object storage/CDN.
- Requires a small abstraction layer and configuration keys (e.g., UPLOAD_DIR, S3_BUCKET, S3_REGION, S3_BASE_URL).
- Adoption steps: add a storage service interface; update controllers to use it; introduce configuration; plan a migration path to S3 when ready; ensure uploads are not committed to git (see ADR-011).