# ADR-002: Architectural Pattern: Electron Main/Renderer Process Model

**Date**: 2025-10-14
**Status**: Proposed

## Context
Electron applications need to manage background tasks (like window management and data persistence) separately from the user interface to ensure responsiveness and security.

## Decision
The application was structured using Electron's standard Main/Renderer process architecture. The Main process (`index.js`) acts as the single source of truth, managing application lifecycle and data I/O. Each window (e.g., the main test window, the leaderboard) runs in an isolated Renderer process.

## Consequences
This creates a clear separation of concerns, making the application more robust and maintainable. It prevents the UI from freezing during disk operations. The trade-off is the added complexity of requiring Inter-Process Communication (IPC) for any interaction between the backend logic and the UI.