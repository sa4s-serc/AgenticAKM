---
### ADR-008: Abstract cloud uploads with provider strategies; implement Google Drive and OneDrive via OAuth2

**Status:** Inferred
**Context:** Uploader includes Strategy abstraction and concrete GoogleDrive.py and OneDrive.py, with OAuth-related files (credentials.json, token.json), google-api-python-client in requirements, and usage logs (gdrive_log.csv).
**Decision:** Implement cloud uploads through a strategy-based abstraction with Google Drive (google-api-python-client) and OneDrive (likely Microsoft Graph via requests) backends using OAuth2 credentials stored locally.
**Consequences:** 
- Positive: Multiple providers supported behind a common interface; easy to add new providers; leverages mature APIs.
- Negative: Storing tokens on disk is a security risk if not protected; provider rate limits and API changes must be handled; requires user consent flows.