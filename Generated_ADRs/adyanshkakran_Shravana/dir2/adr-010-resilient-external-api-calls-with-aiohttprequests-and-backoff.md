---
### ADR-010: Resilient external API calls with aiohttp/requests and backoff

Status: Inferred
Context: requirements.txt includes aiohttp, requests, and backoff. The bot depends on external APIs (Meta, OpenAI) and network calls that may fail transiently.
Decision: Use requests and/or aiohttp for HTTP calls; wrap critical calls with backoff-based retry strategies.
Consequences:
- Positive: Improved reliability under transient failures; better user experience; simpler operational story.
- Negative: Complexity in mixing sync/async patterns; must tune retry policies to avoid rate-limit amplification or long tail latencies.