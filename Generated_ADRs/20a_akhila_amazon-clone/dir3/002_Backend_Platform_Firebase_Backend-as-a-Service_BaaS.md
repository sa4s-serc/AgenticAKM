# ADR-002: Backend Platform: Firebase Backend-as-a-Service (BaaS)

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application needed a backend to handle sensitive operations like payment processing and data persistence without the cost and complexity of provisioning and managing dedicated server infrastructure.

## Decision
Google Firebase was chosen as the comprehensive backend platform. Specifically, Firebase Cloud Functions are used for serverless compute, and Firebase Hosting is used for deploying the frontend.

## Consequences
This choice significantly reduces operational overhead, provides automatic scaling, and offers a pay-per-use cost model beneficial for variable workloads. The main trade-off is vendor lock-in to the Google Cloud ecosystem. There is also a potential for 'cold start' latency on infrequently used functions.