# ADR-011: Mobile app as a UI prototype not coupled to the bot

**Date**: 2025-10-14
**Status**: Proposed

## Context
The Expo/React Native app demonstrates screens and tab navigation but is not a client to the WhatsApp bot.

## Decision
Maintain the mobile app as a separate prototype UI without backend coupling.

## Consequences
Allows independent iteration on UX without backend constraints; limits end-to-end demo capability and may confuse contributors expecting integrated functionality.