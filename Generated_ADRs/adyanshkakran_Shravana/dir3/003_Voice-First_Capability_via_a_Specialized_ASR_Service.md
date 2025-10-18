# ADR-003: Voice-First Capability via a Specialized ASR Service

**Date**: 2025-10-14
**Status**: Proposed

## Context
To improve accessibility and offer a more convenient user experience, the platform needed to support voice input. Given the potential user base in India, a generic speech recognition service might lack accuracy for regional languages and accents.

## Decision
Integrate Automatic Speech Recognition (ASR) by using India's Bhashini API to transcribe audio messages. This capability is a core feature of the WhatsApp bot and is also explored in a standalone script.

## Consequences
This decision makes the platform significantly more accessible and modern. Using a specialized regional API like Bhashini likely provides superior transcription accuracy for the target demographic. It also adds another external dependency, introducing a potential point of failure and latency into the user interaction flow.