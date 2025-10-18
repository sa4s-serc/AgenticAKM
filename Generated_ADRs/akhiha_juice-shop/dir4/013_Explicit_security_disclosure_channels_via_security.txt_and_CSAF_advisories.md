# ADR-013: Explicit security disclosure channels via security.txt and CSAF advisories

**Date**: 2025-10-10
**Status**: Proposed

## Context
Community-facing project must clearly communicate how to report issues and publish advisories.

## Decision
Publish .well-known/security.txt and maintain .well-known/csaf provider metadata and signed advisories.

## Consequences
Benefits: clear, discoverable reporting path; automated tooling compatibility; improved trust. Drawbacks: ongoing maintenance, expectations for timely triage and advisory publication.