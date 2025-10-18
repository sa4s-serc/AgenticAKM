# ADR-008: ASR handled via standalone HTTP pipeline script, not in webhook path

**Date**: 2025-10-14
**Status**: Proposed

## Context
A separate asr.py script posts audio to an external ASR service and returns text; it is not wired into meta/utils.py or the webhook.

## Decision
Keep speech-to-text as an independent utility with explicit integration steps required.

## Consequences
Decouples ASR concerns and simplifies the core webhook; teams can choose when/how to integrate. Adds integration overhead, potential drift in interfaces, and a separate deployment/configuration surface for ASR.