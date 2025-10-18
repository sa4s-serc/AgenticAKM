# ADR-001: Technology Stack Selection: Electron Framework

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project required a cross-platform desktop application to provide a controlled environment for a typing competition. The core functionality involved embedding an existing website (Monkeytype) and managing a local leaderboard.

## Decision
The Electron framework was chosen to build the application. This allows the use of web technologies (HTML, CSS, JavaScript) to create a desktop application, leveraging the bundled Chromium for rendering the UI and Node.js for backend operations like file system access.

## Consequences
This decision enabled rapid development by using a familiar web-based technology stack. It simplified the core requirement of embedding a website. However, it results in a larger application bundle and higher memory consumption compared to a native application, as it includes entire Chromium and Node.js runtimes.