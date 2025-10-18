# ADR-013: Email nudges via Nodemailer and cron using Gmail SMTP

**Date**: 2025-10-16
**Status**: Proposed

## Context
The platform nudges learners with scheduled reminder emails.

## Decision
Send emails with Nodemailer through Gmail SMTP and schedule via node-cron within the server process.

## Consequences
Fast to implement for low volume; Gmail throughput and deliverability limits, brittle OAuth/password setups; in multi-instance deployments, duplicate sends risk without a distributed scheduler; likely migration to a dedicated ESP/queue later.