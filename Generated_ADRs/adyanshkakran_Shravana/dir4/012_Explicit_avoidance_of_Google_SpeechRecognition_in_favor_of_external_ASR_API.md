# ADR-012: Explicit avoidance of Google SpeechRecognition in favor of external ASR API

**Date**: 2025-10-14
**Status**: Proposed

## Context
The ASR flow sends audio to a custom HTTP service defined in asr.py and avoids conflation with Google SpeechRecognition utilities.

## Decision
Standardize on an external HTTP ASR pipeline with language-to-service routing implemented in-house.

## Consequences
Gives control over ASR provider selection and request shaping; introduces dependency on the availability and SLAs of the chosen ASR service and requires custom error handling and monitoring.