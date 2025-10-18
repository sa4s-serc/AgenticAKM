# ADR-005: Internationalization via Java resource bundles

**Date**: 2025-10-14
**Status**: Proposed

## Context
The agent includes messages.properties and messages_fr.properties for i18n.

## Decision
Localize desktop strings using ResourceBundle message properties.

## Consequences
Straightforward localization with minimal runtime overhead; requires disciplined key management and translation workflows; extending to other modules requires consistent i18n patterns.