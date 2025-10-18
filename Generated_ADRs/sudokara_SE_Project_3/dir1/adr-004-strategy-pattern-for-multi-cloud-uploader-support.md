---
### ADR-004: Strategy Pattern for Multi-Cloud Uploader Support

**Status:** Inferred
**Context:** To be a versatile backup tool, the application needed to support uploading backups to various cloud storage providers. Hardcoding a single provider would severely limit the tool's utility. The challenge was to create a flexible architecture that could accommodate different cloud APIs and authentication mechanisms.
**Decision:** The Strategy design pattern was chosen to manage uploads to different cloud storage providers. The `src/phoenix/Uploader/` directory contains:
*   An abstract strategy or interface, suggested by `Strategy.py`.
*   Concrete implementations for `GoogleDrive.py` and `OneDrive.py`.
The dependencies listed in `requirements.txt`, such as `google-api-python-client` and `google-auth-oauthlib`, directly support the implementation of the Google Drive strategy.
**Consequences:**
*   **Positive:**
    *   **Extensibility:** Adding support for a new cloud provider (e.g., Dropbox, S3) only requires creating a new strategy class that conforms to the uploader interface. The core application logic remains unchanged.
    *   **User Choice:** End-users can configure and choose their preferred cloud storage destination.
*   **Negative:**
    *   **Implementation Overhead:** Each new provider requires dedicated code to handle its specific API, authentication flow, and error handling, which can be a significant development effort.
    *   **Credential Management Complexity:** The system must securely manage different types of credentials and tokens (e.g., `token.json`, `credentials.json`) for each supported service.