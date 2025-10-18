---
### ADR-006: Support on-the-fly media transcoding and HTTP range streaming

Status: Inferred
Context: TranscoderService, TranscodedInputStream, ffmpeg installation in Docker, and MediaStreamer for HTTP range requests exist. Config/Transcoder entities stored in DB.
Decision: Use ffmpeg for server-side transcoding pipelines and serve audio with HTTP range support to enable browser/clients to seek within streams.
Consequences:
- Positive: Broad codec/device compatibility; adaptive performance by transcoding to target formats/bitrates; seek support improves UX.
- Negative: CPU-intensive workloads; need for careful process management and timeout handling; operational dependency on ffmpeg availability/version.