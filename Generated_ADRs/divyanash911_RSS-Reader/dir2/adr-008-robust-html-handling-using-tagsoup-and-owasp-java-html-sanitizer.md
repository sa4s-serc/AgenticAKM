---
### ADR-008: Robust HTML handling using TagSoup and OWASP Java HTML Sanitizer

Status: Inferred
Context: Dependencies include TagSoup 1.2.1 and OWASP Java HTML Sanitizer (r156), typical choices for dealing with untrusted/malformed HTML content (e.g., RSS entries).
Decision: Parse leniently with TagSoup and sanitize with OWASP Java HTML Sanitizer to mitigate XSS and formatting issues in feed content.
Consequences:
- Positive: Increased resilience to malformed inputs and improved security against content-based attacks.
- Negative: Runtime overhead for parsing/sanitizing; sanitization policies require maintenance and testing.