# ADR-002: Flask-based webhook for WhatsApp integration

**Date**: 2025-10-14
**Status**: Proposed

## Context
Incoming WhatsApp Business events are received and processed via a Flask blueprint exposing the webhook endpoint.

## Decision
Use Flask to implement the webhook layer with GET for verification and POST for event processing.

## Consequences
Provides a simple, well-understood HTTP surface for Meta callbacks and is easy to host; however, it relies on synchronous request handling and single-process semantics unless scaled behind a proper WSGI setup or background workers.