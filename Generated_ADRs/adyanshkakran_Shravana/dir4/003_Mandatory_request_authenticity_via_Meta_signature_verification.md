# ADR-003: Mandatory request authenticity via Meta signature verification

**Date**: 2025-10-14
**Status**: Proposed

## Context
A decorator validates incoming POST requests to ensure they originate from Meta and not arbitrary clients.

## Decision
Enforce X-Hub signature validation and verification token checks on the webhook endpoints.

## Consequences
Strengthens security and integrity of the webhook; misconfiguration of secrets or token mismatches will cause legitimate traffic to be rejected, increasing operational sensitivity to environment configuration.