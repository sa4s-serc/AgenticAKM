# ADR-018: In-process scheduling for background jobs

**Date**: 2025-10-16
**Status**: Proposed

## Context
email_nudge.js indicates cron-ready scheduling within the API runtime.

## Decision
Run scheduled jobs in-process using node-cron rather than an external scheduler or queue.

## Consequences
Low operational overhead for a single instance; risks duplicate executions and clock drift at scale; migration to a distributed scheduler or message queue will be needed as load grows.