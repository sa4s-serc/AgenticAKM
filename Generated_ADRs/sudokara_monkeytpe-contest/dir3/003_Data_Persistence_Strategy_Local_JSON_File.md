# ADR-003: Data Persistence Strategy: Local JSON File

**Date**: 2025-10-14
**Status**: Proposed

## Context
A simple, serverless, and persistent storage mechanism was needed to store the leaderboard scores locally on the user's machine.

## Decision
A single JSON file (`leaderboard.json`) was chosen as the data store. The Main process has exclusive responsibility for all read and write operations, ensuring data integrity and centralizing data management logic.

## Consequences
This approach is extremely simple to implement and requires no external database dependencies, making the application self-contained. The data is human-readable and easy to inspect. However, this method is not scalable for high-frequency writes or large datasets, as the entire file must be read and rewritten on every update.