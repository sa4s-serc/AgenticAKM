# ADR-005: Third-Party Content Integration: Webview Tag for Sandboxing

**Date**: 2025-10-14
**Status**: Proposed

## Context
The application's core feature is running a typing test from the official Monkeytype website. This external content needed to be embedded within the application's UI in a controlled and isolated manner.

## Decision
The `<webview>` tag was used to embed the Monkeytype website. This loads the external content in a separate process, effectively sandboxing it from the application's main renderer process, which is necessary for security and stability.

## Consequences
This decision greatly simplifies development by reusing a high-quality, existing web service instead of building a typing test from scratch. The sandboxing provides security benefits. The major drawback is a brittle dependency on the Monkeytype website's DOM structure; any change to the site's layout could break the application's result-scraping logic.