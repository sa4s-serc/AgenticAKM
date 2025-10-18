# ADR-001: Cross‑platform desktop stack

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application must run as a desktop app and render a web-based typing UI with a leaderboard.

## Decision
Build the app with Electron, using a main process (index.js), HTML renderer entry points (index.html, leaderboard.html) with corresponding scripts, and a preload bridge (preload.js).

## Consequences
Enables reuse of web technologies and cross‑platform distribution, but increases memory/CPU footprint compared to native stacks and requires careful IPC/security hardening between main and renderers.