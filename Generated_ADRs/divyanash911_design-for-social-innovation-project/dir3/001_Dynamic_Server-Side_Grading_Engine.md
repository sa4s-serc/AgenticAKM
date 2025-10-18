# ADR-001: Dynamic Server-Side Grading Engine

**Date**: 2025-10-13
**Status**: Proposed

## Context
The core requirement was to support complex, customizable, and nuanced scoring for questionnaires, beyond simple point allocation. The assessment logic needed to be adaptable by non-developer domain experts (e.g., psychologists) without requiring backend code deployments for each new rubric.

## Decision
A feature was implemented to allow authorized users to write and save Python scripts directly in the UI. The Flask backend was architected to securely receive these scripts as strings, execute them in a controlled environment against user responses, and return the calculated score.

## Consequences
This provides immense flexibility and empowers domain experts to create sophisticated assessment models. However, it introduces a critical security risk by executing user-provided code. This necessitates robust sandboxing, resource limiting, and input sanitization to prevent code injection, denial-of-service attacks, or data breaches. It also adds complexity to debugging, as errors could be in user scripts rather than the core application.