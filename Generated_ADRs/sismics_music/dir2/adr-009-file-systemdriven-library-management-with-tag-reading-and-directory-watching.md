---
### ADR-009: File-system–driven library management with tag reading and directory watching

Status: Inferred
Context: CollectionService and CollectionWatchService scan/watch directories; DirectoryNameParser and ImportAudio/ImportAudioService handle ingest; JAudioTagger is used in core and Android; album art services manage on-disk images.
Decision: Treat the file system as the source of truth; watch configured directories, import new/changed files, parse tags and album art, and update the library accordingly.
Consequences:
- Positive: Minimal user input; automatic sync with existing folders; consistent metadata extraction across platforms.
- Negative: Handling of edge cases (corrupted tags, odd directory structures); platform-specific file watching differences; potential latency between change and availability.