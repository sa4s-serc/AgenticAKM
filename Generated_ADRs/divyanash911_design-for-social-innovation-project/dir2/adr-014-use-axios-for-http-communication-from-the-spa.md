---
### ADR-014: Use Axios for HTTP communication from the SPA

Status: Inferred
Context: axios is a dependency; custom hooks (e.g., FetchQuestion, FetchChildren) likely wrap network calls.
Decision: Standardize on Axios for REST API requests from React.
Consequences:
- Positive: Consistent HTTP client with interceptors, cancellation, and error handling; widely used.
- Negative: Another dependency vs native fetch; must manage typing and response normalization manually.