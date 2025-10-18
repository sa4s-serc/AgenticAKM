# ADR-001: Split architecture: WhatsApp bot backend and Expo/React Native app are independent

**Date**: 2025-10-14
**Status**: Proposed

## Context
The repository contains a Python-based WhatsApp bot and an Expo/React Native mobile app that serve different purposes and are not wired together.

## Decision
Keep the bot backend and the mobile UI as separate, largely independent parts within the same repository.

## Consequences
Enables independent development and deployment lifecycles, reduces coupling, and clarifies responsibilities; however, it may cause confusion about end-to-end integration and requires clear documentation to prevent assumptions that the app is a client for the bot.