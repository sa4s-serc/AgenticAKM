# ADR-009: Transport Details Hidden with Extension Points

**Date**: 2025-10-14
**Status**: Proposed

## Context
Clients need to customize behavior without tightly coupling to the transport stack.

## Decision
Hide transport internals and expose extension points via plugins, endpoint/request closures, and custom TargetType/Endpoint strategies.

## Consequences
Pros: Flexible adaptation for headers, retries, caching, and analytics without forking core. Cons: Deep socket/session tuning still requires Alamofire or URLSession-level changes, potential for leaky abstractions in advanced scenarios.