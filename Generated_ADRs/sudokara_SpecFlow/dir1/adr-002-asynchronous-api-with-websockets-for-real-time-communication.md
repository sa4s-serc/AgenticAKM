---
### ADR-002: Asynchronous API with WebSockets for Real-time Communication

**Status:** Inferred
**Context:** The speculative decoding architecture requires a highly responsive, low-latency communication channel between the edge client and the cloud server. A traditional synchronous, request-response (e.g., RESTful HTTP) protocol would be inefficient for streaming data or for the rapid back-and-forth verification of speculative tokens.
**Decision:** An asynchronous API built with FastAPI, Uvicorn, and WebSockets was chosen for the communication layer. The inclusion of `fastapi`, `uvicorn`, and `websockets` in the requirements points to a modern, high-performance ASGI-based stack. The `httpx` library is likely used on the client-side for making asynchronous requests. The existence of `common/protocol.py` suggests a custom application-level protocol is defined over this WebSocket transport layer.
**Consequences:**
*   **Positive:**
    *   Enables full-duplex, real-time communication, which is ideal for the speculative decoding use case.
    *   Reduces network overhead and latency compared to repeatedly establishing HTTP connections.
    *   FastAPI provides high performance and modern features like automatic data validation via Pydantic.
*   **Negative:**
    *   WebSocket-based communication is more stateful and complex to manage than stateless REST APIs.
    *   Firewalls and proxies can sometimes interfere with WebSocket connections, potentially complicating deployment (`configure_firewall.bat` may be related to this).