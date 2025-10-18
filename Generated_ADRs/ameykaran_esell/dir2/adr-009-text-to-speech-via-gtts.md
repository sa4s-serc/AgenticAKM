---
### ADR-009: Text-to-Speech via gTTS

Status: Inferred
Context: gTTS is a dependency; backend/audio.py exists; pydub/mutagen included for audio processing/metadata.
Decision: Use Google Text-to-Speech (gTTS) for generating narration audio locally.
Consequences:
- Positive: Simple API; no separate paid TTS service required; offline-friendly once installed.
- Negative: Voice quality and language coverage limitations vs premium TTS; rate limits/connectivity considerations.