---
### ADR-013: Support offline/fallback notes on the client in addition to server-stored notes

Status: Inferred
Context: The frontend contains data/userNotes.json and utilities clientNotesUtils.ts and notesUtils.ts, alongside server-side note models and routes.
Decision: Provide client-side notes storage as a fallback or offline-first experience, with server synchronization where available.
Consequences:
- Positive: Better UX in unreliable networks; local-first interactions.
- Negative: Sync conflicts and reconciliation complexity; duplication of logic across client and server.