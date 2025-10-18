---
### ADR-003: Event-driven I/O using libev

Status: Inferred
Context: FindLibev.cmake and http.c, network.c point to an event-driven HTTP server for metrics exposure. Exporters benefit from non-blocking I/O to handle concurrent scrapes and backend connections efficiently.
Decision: Use libev to implement an event-driven networking model for HTTP and connection handling.
Consequences:
- Positive: Efficient concurrency with low overhead; scales with many simultaneous connections; simpler than thread-per-connection.
- Negative: Requires careful non-blocking programming; debugging event loops can be complex.