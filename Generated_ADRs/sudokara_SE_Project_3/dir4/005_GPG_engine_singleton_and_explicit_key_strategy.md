# ADR-005: GPG engine singleton and explicit key strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
Encryption requires consistent handling of the GPG engine and keys across the process and operations.

## Decision
Use a GPGSingleton for engine lifecycle and a GPGKeyStrategy for key generation/management, backed by python-gnupg and a local keyring.

## Consequences
Simplifies reuse and avoids repeated initialization; centralizes key operations; singleton may constrain concurrency or testing; local keyring and passphrase handling must be secured and documented.