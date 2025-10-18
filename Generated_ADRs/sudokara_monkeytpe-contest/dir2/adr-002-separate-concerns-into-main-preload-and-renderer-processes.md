---
### ADR-002: Separate concerns into Main, Preload, and Renderer processes

Status: Inferred
Context: Presence of index.js (main), preload.js, and renderer.js indicates the standard Electron architecture to isolate browser (renderer) from Node and OS access, mediating communications via a preload bridge.
Decision: Use a preload script to expose a minimal, controlled API from the main process to renderer processes (likely via IPC), keeping business logic and privileged operations out of the renderer.
Consequences:
- Positive: Improved security by limiting renderer privileges; clearer separation of responsibilities; easier to audit privileged operations.
- Negative: Additional complexity in IPC and API surface design; debugging across process boundaries is more complex.