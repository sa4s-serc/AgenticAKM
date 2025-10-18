# ADR-002: User Authentication and Identity Management

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application is tailored for a trusted, closed community like a university, which typically operates its own centralized identity management system. A secure, reliable, and convenient authentication method was necessary without reinventing the wheel.

## Decision
Authentication is delegated to an external Central Authentication Service (CAS) via a Single Sign-On (SSO) mechanism. The application does not store or manage user passwords, only creating a local profile after a successful external authentication.

## Consequences
This is a strong security decision, offloading critical password management to a robust, dedicated system. It enhances user experience by leveraging existing institutional credentials. The main trade-off is a hard dependency on the availability of the external CAS; if the CAS is down, users cannot access the application.