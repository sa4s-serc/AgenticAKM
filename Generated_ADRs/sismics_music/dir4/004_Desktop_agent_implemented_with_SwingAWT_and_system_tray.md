# ADR-004: Desktop agent implemented with Swing/AWT and system tray

**Date**: 2025-10-14
**Status**: Proposed

## Context
The music-agent module includes UI classes (AgentFrame, TrayController) and utilities indicating Swing/AWT usage.

## Decision
Build the desktop agent UI with Swing/AWT, including a system tray controller, and integrate deployment orchestration within the agent.

## Consequences
Delivers a lightweight, cross-platform desktop UI without external UI runtimes; UX is dated and harder to modernize; tray features vary across OSes; long-term maintenance requires Java desktop expertise.