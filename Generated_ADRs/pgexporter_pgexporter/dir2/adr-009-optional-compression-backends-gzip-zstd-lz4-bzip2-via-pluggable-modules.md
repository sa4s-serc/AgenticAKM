---
### ADR-009: Optional compression backends (gzip, zstd, lz4, bzip2) via pluggable modules

Status: Inferred
Context: Multiple compression modules and Find*.cmake files for zstd, lz4, bzip2; gzip support present. HTTP servers often benefit from content compression.
Decision: Provide optional compression algorithms as pluggable components enabled if libraries are available.
Consequences:
- Positive: Flexible performance/size trade-offs; takes advantage of faster algorithms (zstd/lz4) when present.
- Negative: Larger code surface; conditional builds add complexity; runtime negotiation/configuration required.