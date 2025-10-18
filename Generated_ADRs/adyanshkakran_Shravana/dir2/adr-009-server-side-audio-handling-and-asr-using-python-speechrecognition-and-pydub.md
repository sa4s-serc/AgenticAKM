---
### ADR-009: Server-side audio handling and ASR using Python SpeechRecognition and pydub

Status: Inferred
Context: The repo includes asr.py, SpeechRecognition and pydub dependencies, and .ogg files under the Flask instance directory. WhatsApp voice notes are typically OGG/Opus, requiring decoding/transcoding.
Decision: Implement audio ingestion, normalization/transcoding (via pydub), and speech-to-text (via SpeechRecognition) on the server; store temporary audio under Flask’s instance directory.
Consequences:
- Positive: Centralized ASR pipeline; control over formats; supports WhatsApp voice workflows.
- Negative: Server CPU/memory usage for audio processing; codec edge cases; potential latency; storage management for temp files.