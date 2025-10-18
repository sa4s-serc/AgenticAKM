# ADR-001: Decoupled Client-Server Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system required a way for users to manage a central music library from both a desktop environment (for server setup) and a mobile device (for playback and control). A monolithic application would not meet these distinct needs.

## Decision
A three-component client-server architecture was implemented: a central (but absent) server application, a dedicated Java desktop agent (`music-agent`) for server deployment and management, and a native Android client (`music-android`) for remote user interaction.

## Consequences
This separation of concerns allows the server to run as a headless service on any suitable machine, while providing tailored user experiences for administration and playback. However, it increases overall system complexity, requiring maintenance of three distinct codebases and a stable API between the server and its clients.