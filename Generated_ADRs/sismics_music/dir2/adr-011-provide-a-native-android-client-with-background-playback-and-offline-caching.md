---
### ADR-011: Provide a native Android client with background playback and offline caching

Status: Inferred
Context: music-android includes a MusicService with AudioFocus handling, EventBus integration, offline caching utilities (CacheUtil), local storage (SnappyDB + Kryo), and UI fragments for albums/playlists/playing.
Decision: Deliver a native Android application that communicates with the server APIs, manages playback in a foreground service, and caches tracks for offline use; use EventBus for intra-app decoupling.
Consequences:
- Positive: Better mobile UX and platform integration; offline mode; modular components via event bus.
- Negative: Additional client maintenance; cache consistency concerns; reliance on deprecated support libraries (28.x).