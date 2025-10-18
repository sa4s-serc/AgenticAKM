# ADR-010: Production hosting assumption: public HTTPS with Meta webhook verification

**Date**: 2025-10-14
**Status**: Proposed

## Context
Meta requires publicly reachable HTTPS endpoints with verification token handshake for webhook registration.

## Decision
Design the webhook to run on an internet-accessible HTTPS endpoint with verification enabled.

## Consequences
Supports real WhatsApp traffic and Meta onboarding; adds operational requirements for TLS termination and exposes the need for tunneling (e.g., ngrok) or cloud hosting during development.