# ADR-003: Client-Side GPG Encryption

**Date**: 2025-10-14
**Status**: Proposed

## Context
A critical requirement was to ensure the privacy and security of user data, especially since it would be stored on third-party cloud services. The decision centered on where and how to apply encryption to create a zero-knowledge system.

## Decision
A mandatory client-side encryption step was integrated into the backup pipeline using GnuPG (GPG). Files are encrypted on the user's local machine using public-key cryptography before they are uploaded to any external storage.

## Consequences
This approach provides a strong security guarantee, as the cloud provider never has access to the unencrypted data, ensuring user privacy. However, it places the full responsibility of key management on the user; loss of the private GPG key results in irrecoverable data.