---
### ADR-008: Local Server File System for Media Storage

**Status:** Inferred

**Context:** The application requires a way to store uploaded files, such as images for food items. A simple and direct method for handling these uploads from the backend was needed.

**Decision:** The application stores uploaded files directly on the local file system of the backend server. This is inferred from the `multer` dependency, which handles `multipart/form-data` uploads, and the existence of the `backend/uploads` directory containing image files with timestamped names.

**Consequences:**
*   **Positive:**
    *   Simple to implement and requires no external services or additional configuration for a single-server setup.
    *   No direct costs associated with file storage, unlike cloud storage services.
*   **Negative:**
    *   This approach is not scalable. In a multi-server or load-balanced environment, files uploaded to one server instance will not be available on others.
    *   In many modern cloud/containerized environments (like Heroku or Docker), the local file system is ephemeral, meaning uploaded files would be lost upon server restart or redeployment.
    *   Makes server backups and migrations more complex, as the file storage directory must be manually handled. This solution is generally unsuitable for a production application that needs to be scalable and durable.