# ADR-005: Command-Line Interface (CLI) as Primary User Interface

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system needed an interface for users to configure, control, and manage the backup and recovery processes. The choice of interface type (GUI, Web, CLI) would define the primary user experience and integration capabilities.

## Decision
A comprehensive Command-Line Interface (CLI) was chosen as the primary means of user interaction. It handles all setup, configuration, and operational commands.

## Consequences
The CLI is lightweight, scriptable, and ideal for automation, appealing to power users and for use in server environments. This decision decouples the core backend logic from any specific presentation layer, allowing a GUI or other interface to be built on top later without altering the core system.