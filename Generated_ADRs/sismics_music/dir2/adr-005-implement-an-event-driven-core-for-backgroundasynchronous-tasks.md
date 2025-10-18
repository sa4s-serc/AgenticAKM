---
### ADR-005: Implement an event-driven core for background/asynchronous tasks

Status: Inferred
Context: music-core defines async events/listeners (e.g., CollectionReindexAsyncEvent, PlayStarted/Completed, TrackLiked/Unliked, LastFm updates) and listeners under listener.async. Guava is a dependency; AppContext suggests centralized context wiring.
Decision: Use an internal event bus pattern to decouple producers (e.g., play events, import triggers) from consumers (indexing, scrobbling, metadata updates), processing tasks asynchronously.
Consequences:
- Positive: Loose coupling; improved responsiveness; easier extension of side-effects without changing core flows.
- Negative: Harder troubleshooting (eventual consistency, ordering); need for robust error handling and visibility into background processing.